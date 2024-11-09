# necessary for annotating constructors
from __future__ import annotations

from dataclasses import dataclass, Field

from itertools import chain
from typing import Any, Callable, Dict, Iterator, List, Type, TypeVar

from dbt_common.contracts.config.metadata import Metadata
from dbt_common.exceptions import CompilationError, DbtInternalError
from dbt_common.contracts.config.properties import AdditionalPropertiesAllowed
from dbt_common.contracts.util import Replaceable

T = TypeVar("T", bound="BaseConfig")


@dataclass
class BaseConfig(AdditionalPropertiesAllowed, Replaceable):
    # enable syntax like: config['key']
    def __getitem__(self, key: str) -> Any:
        return self.get(key)

    # like doing 'get' on a dictionary
    def get(self, key: str, default: Any = None) -> Any:
        if hasattr(self, key):
            return getattr(self, key)
        elif key in self._extra:
            return self._extra[key]
        else:
            return default

    # enable syntax like: config['key'] = value
    def __setitem__(self, key: str, value) -> None:
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            self._extra[key] = value

    def __delitem__(self, key: str) -> None:
        if hasattr(self, key):
            msg = (
                'Error, tried to delete config key "{}": Cannot delete ' "built-in keys"
            ).format(key)
            raise CompilationError(msg)
        else:
            del self._extra[key]

    def _content_iterator(self, include_condition: Callable[[Field[Any]], bool]) -> Iterator[str]:
        seen = set()
        for fld, _ in self._get_fields():
            seen.add(fld.name)
            if include_condition(fld):
                yield fld.name

        for key in self._extra:
            if key not in seen:
                seen.add(key)
                yield key

    def __iter__(self) -> Iterator[str]:
        yield from self._content_iterator(include_condition=lambda f: True)

    def __len__(self) -> int:
        return len(self._get_fields()) + len(self._extra)

    @staticmethod
    def compare_key(
        unrendered: Dict[str, Any],
        other: Dict[str, Any],
        key: str,
    ) -> bool:
        if key not in unrendered and key not in other:
            return True
        elif key not in unrendered and key in other:
            return False
        elif key in unrendered and key not in other:
            return False
        else:
            return bool(unrendered[key] == other[key])

    @classmethod
    def same_contents(cls, unrendered: Dict[str, Any], other: Dict[str, Any]) -> bool:
        """This is like __eq__, except it ignores some fields."""
        seen = set()
        for fld, target_name in cls._get_fields():
            key = target_name
            seen.add(key)
            if CompareBehavior.should_include(fld):
                if not cls.compare_key(unrendered, other, key):
                    return False

        for key in chain(unrendered, other):
            if key not in seen:
                seen.add(key)
                if not cls.compare_key(unrendered, other, key):
                    return False
        return True

    # This is used in 'merge_config_dicts' to create the combined orig_dict.
    # Note: "clobber" fields aren't defined, because that's the default.
    #    "access" is currently the only Clobber field.
    # This shouldn't really be defined  here. It would be better to have it
    # associated with the config definitions, but at the point we use it, we
    # don't know which config we're dealing with.
    mergebehavior = {
        "append": ["pre-hook", "pre_hook", "post-hook", "post_hook", "tags", "packages"],
        "update": [
            "quoting",
            "column_types",
            "meta",
            "docs",
            "contract",
        ],
        "dict_key_append": ["grants"],
        "object": ["snapshot_meta_column_names"],
    }

    @classmethod
    def _merge_dicts(cls, src: Dict[str, Any], data: Dict[str, Any]) -> Dict[str, Any]:
        """Mutate input to return merge results.

        Find all the items in data that match a target_field on this class,
        and merge them with the data found in `src` for target_field, using the
        field's specified merge behavior. Matching items will be removed from
        `data` (but _not_ `src`!).

        Returns a dict with the merge results.

        That means this method mutates its input! Any remaining values in data
        were not merged.
        """
        result = {}

        for fld, target_field in cls._get_fields():
            if target_field not in data:
                continue

            data_attr = data.pop(target_field)
            if target_field not in src:
                result[target_field] = data_attr
                continue

            merge_behavior = MergeBehavior.from_field(fld)
            self_attr = src[target_field]

            result[target_field] = _merge_field_value(
                merge_behavior=merge_behavior,
                self_value=self_attr,
                other_value=data_attr,
            )
        return result

    def update_from(
        self: T, data: Dict[str, Any], config_cls: Type[BaseConfig], validate: bool = True
    ) -> T:
        """Update and validate config given a dict.

        Given a dict of keys, update the current config from them, validate
        it, and return a new config with the updated values
        """
        dct = self.to_dict(omit_none=False)

        self_merged = self._merge_dicts(dct, data)
        dct.update(self_merged)

        adapter_merged = config_cls._merge_dicts(dct, data)
        dct.update(adapter_merged)

        # any remaining fields must be "clobber"
        dct.update(data)

        # any validation failures must have come from the update
        if validate:
            self.validate(dct)
        return self.from_dict(dct)

    def finalize_and_validate(self: T) -> T:
        dct = self.to_dict(omit_none=False)
        self.validate(dct)
        return self.from_dict(dct)


class MergeBehavior(Metadata):
    Append = 1
    Update = 2
    Clobber = 3
    DictKeyAppend = 4
    Object = 5

    @classmethod
    def default_field(cls) -> "MergeBehavior":
        return cls.Clobber

    @classmethod
    def metadata_key(cls) -> str:
        return "merge"


class CompareBehavior(Metadata):
    Include = 1
    Exclude = 2

    @classmethod
    def default_field(cls) -> "CompareBehavior":
        return cls.Include

    @classmethod
    def metadata_key(cls) -> str:
        return "compare"

    @classmethod
    def should_include(cls, fld: Field[Any]) -> bool:
        return cls.from_field(fld) == cls.Include


def _listify(value: Any) -> List[Any]:
    if isinstance(value, list):
        return value[:]
    else:
        return [value]


# There are two versions of this code. The one here is for config
# objects which can get the "MergeBehavior" from the field in the class,
# the one below in 'merge_config_dicts' (formerly in
# _add_config_call in core context_config.py) is for config_call dictionaries
# where we need to get the MergeBehavior from someplace else.
def _merge_field_value(
    merge_behavior: MergeBehavior,
    self_value: Any,
    other_value: Any,
) -> Any:
    if merge_behavior == MergeBehavior.Clobber:
        return other_value
    elif merge_behavior == MergeBehavior.Append:
        new_value = _listify(self_value) + _listify(other_value)
        return new_value
    elif merge_behavior == MergeBehavior.Update:
        if not isinstance(self_value, dict):
            raise DbtInternalError(f"expected dict, got {self_value}")
        if not isinstance(other_value, dict):
            raise DbtInternalError(f"expected dict, got {other_value}")
        value = self_value.copy()
        value.update(other_value)
        return value
    elif merge_behavior == MergeBehavior.DictKeyAppend:
        if not isinstance(self_value, dict):
            raise DbtInternalError(f"expected dict, got {self_value}")
        if not isinstance(other_value, dict):
            raise DbtInternalError(f"expected dict, got {other_value}")
        new_dict = {}
        for key in self_value.keys():
            new_dict[key] = _listify(self_value[key])
        for key in other_value.keys():
            extend = False
            new_key = key
            # This might start with a +, to indicate we should extend the list
            # instead of just clobbering it
            if new_key.startswith("+"):
                new_key = key.lstrip("+")
                extend = True
            if new_key in new_dict and extend:
                # extend the list
                value = other_value[key]
                new_dict[new_key].extend(_listify(value))
            else:
                # clobber the list
                new_dict[new_key] = _listify(other_value[key])
        return new_dict
    elif merge_behavior == MergeBehavior.Object:
        # All fields in classes with MergeBehavior.Object should have a default of None
        if not type(self_value).__name__ == type(other_value).__name__:
            raise DbtInternalError(
                f"got conflicting types: {type(self_value).__name__} and {type(other_value).__name__}"
            )
        new_value = self_value.copy()
        new_value.update(other_value)
        return new_value
    else:
        raise DbtInternalError(f"Got an invalid merge_behavior: {merge_behavior}")


# This is used in ContextConfig._add_config_call. It updates the orig_dict in place.
def merge_config_dicts(orig_dict: Dict[str, Any], new_dict: Dict[str, Any]) -> None:
    # orig_dict is already encountered configs, new_dict is new
    # This mirrors code in _merge_field_value in model_config.py which is similar but
    # operates on config objects.
    if orig_dict == {}:
        orig_dict.update(new_dict)
        return
    for k, v in new_dict.items():
        # MergeBehavior for post-hook and pre-hook is to collect all
        # values, instead of overwriting
        if k in BaseConfig.mergebehavior["append"]:
            if k in orig_dict:  # should always be a list here
                orig_dict[k] = _listify(orig_dict[k]) + _listify(v)
            else:
                orig_dict[k] = _listify(v)
        elif k in BaseConfig.mergebehavior["update"]:
            if not isinstance(v, dict):
                raise DbtInternalError(f"expected dict, got {v}")
            if k in orig_dict and isinstance(orig_dict[k], dict):
                orig_dict[k].update(v)
            else:
                orig_dict[k] = v
        elif k in BaseConfig.mergebehavior["dict_key_append"]:
            if not isinstance(v, dict):
                raise DbtInternalError(f"expected dict, got {v}")
            if k in orig_dict:  # should always be a dict
                for key in orig_dict[k].keys():
                    orig_dict[k][key] = _listify(orig_dict[k][key])
                for key, value in v.items():
                    extend = False
                    # This might start with a +, to indicate we should extend the list
                    # instead of just clobbering it. We don't want to remove the + here
                    # (like in the other method) because we want it preserved
                    if key.startswith("+"):
                        extend = True
                    if key in orig_dict[k] and extend:
                        # extend the list
                        orig_dict[k][key].extend(_listify(value))
                    else:
                        # clobber the list
                        orig_dict[k][key] = _listify(value)
            else:
                # This is always a dictionary
                orig_dict[k] = v
                # listify everything
                for key, value in orig_dict[k].items():
                    orig_dict[k][key] = _listify(value)
        elif k in BaseConfig.mergebehavior["object"]:
            if not isinstance(v, dict):
                raise DbtInternalError(f"expected dict, got {v}")
            if k not in orig_dict:
                orig_dict[k] = {}
            for obj_k, obj_v in v.items():
                orig_dict[k][obj_k] = obj_v
        else:  # Clobber
            orig_dict[k] = v
