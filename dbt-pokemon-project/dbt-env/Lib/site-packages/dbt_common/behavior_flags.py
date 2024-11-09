import inspect
from typing import Any, Dict, List, TypedDict

try:
    from typing import NotRequired
except ImportError:
    # NotRequired was introduced in Python 3.11
    # This is the suggested way to implement a TypedDict with optional arguments
    from typing import Optional as NotRequired

from dbt_common.events.functions import fire_event
from dbt_common.events.types import BehaviorChangeEvent
from dbt_common.exceptions import CompilationError, DbtInternalError


class BehaviorFlag(TypedDict):
    """
    Configuration used to create a BehaviorFlagRendered instance

    Args:
        name: the name of the behavior flag
        default: default setting, starts as False, becomes True after a bake-in period
        description: an additional message to send when the flag evaluates to False
        docs_url: the url to the relevant docs on docs.getdbt.com

    *Note*:
        While `description` and `docs_url` are both listed as `NotRequired`, at least one of them is required.
        This is validated when the flag is rendered in `BehaviorFlagRendered` below.
        The goal of this restriction is to provide the end user with context so they can make an informed decision
        about if, and when, to enable the behavior flag.
    """

    name: str
    default: bool
    source: NotRequired[str]
    description: NotRequired[str]
    docs_url: NotRequired[str]


class BehaviorFlagRendered:
    """
    A rendered behavior flag that gets used throughout dbt packages

    Args:
        flag: the configuration for the behavior flag
        user_overrides: a set of user settings, one of which may be an override on this behavior flag
    """

    fired: bool = False

    def __init__(self, flag: BehaviorFlag, user_overrides: Dict[str, Any]) -> None:
        self._validate(flag)

        self.name = flag["name"]
        self.setting = user_overrides.get(flag["name"], flag["default"])

        default_description = (
            f"""The behavior controlled by `{flag["name"]}` is currently turned off.\n"""
        )
        default_docs_url = "https://docs.getdbt.com/reference/global-configs/behavior-changes"
        self._behavior_change_event = BehaviorChangeEvent(
            flag_name=flag["name"],
            flag_source=flag.get("source", self._default_source()),
            description=flag.get("description", default_description),
            docs_url=flag.get("docs_url", default_docs_url),
        )

    @staticmethod
    def _validate(flag: BehaviorFlag) -> None:
        if flag.get("description") is None and flag.get("docs_url") is None:
            raise DbtInternalError(
                "Behavior change flags require at least one of `description` and `docs_url`."
            )

    @property
    def setting(self) -> bool:
        if self._setting is False and not self.fired:
            fire_event(self._behavior_change_event)
            self.fired = True
        return self._setting

    @setting.setter
    def setting(self, value: bool) -> None:
        self._setting = value

    @property
    def no_warn(self) -> bool:
        return self._setting

    @staticmethod
    def _default_source() -> str:
        """
        If the maintainer did not provide a source, default to the module that called this class.
        For adapters, this will likely be `dbt.adapters.<foo>.impl` for `dbt-foo`.
        """
        for frame in inspect.stack():
            if module := inspect.getmodule(frame[0]):
                if module.__name__ != __name__:
                    return module.__name__
        return "Unknown"

    def __bool__(self) -> bool:
        return self.setting


class Behavior:
    """
    A collection of behavior flags

    This is effectively a dictionary that supports dot notation for easy reference, e.g.:
        ```python
        if adapter.behavior.my_flag:
            ...

        if adapter.behavior.my_flag.no_warn:  # this will not fire the behavior change event
            ...
        ```
        ```jinja
        {% if adapter.behavior.my_flag %}
            ...
        {% endif %}

        {% if adapter.behavior.my_flag.no_warn %}  {# this will not fire the behavior change event #}
            ...
        {% endif %}
        ```

    Args:
        flags: a list of configurations, one for each behavior flag
        user_overrides: a set of user settings, which may include overrides on one or more of the behavior flags
    """

    _flags: List[BehaviorFlagRendered]

    def __init__(self, flags: List[BehaviorFlag], user_overrides: Dict[str, Any]) -> None:
        self._flags = [BehaviorFlagRendered(flag, user_overrides) for flag in flags]

    def __getattr__(self, name: str) -> BehaviorFlagRendered:
        for flag in self._flags:
            if flag.name == name:
                return flag
        raise CompilationError(f"The flag {name} has not be registered.")
