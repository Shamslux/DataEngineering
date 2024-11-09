import dataclasses
from typing import Any, TypeVar

_R = TypeVar("_R", bound="Replaceable")


# TODO: remove from dbt_common.contracts.util:: Replaceable + references
class Replaceable:
    def replace(self: _R, **kwargs: Any) -> _R:
        return dataclasses.replace(self, **kwargs)  # type: ignore


_M = TypeVar("_M", bound="Mergeable")


class Mergeable(Replaceable):
    def merged(self: _M, *args: Any) -> _M:
        """Perform a shallow merge, where the last non-None write wins. This is
        intended to merge dataclasses that are a collection of optional values.
        """
        replacements = {}
        cls = type(self)
        for arg in args:
            for field in dataclasses.fields(cls):  # type: ignore
                value = getattr(arg, field.name)
                if value is not None:
                    replacements[field.name] = value

        return self.replace(**replacements)
