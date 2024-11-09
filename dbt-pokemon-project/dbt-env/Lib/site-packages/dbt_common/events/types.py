from dbt_common.events.base_types import (
    DebugLevel,
    InfoLevel,
    WarnLevel,
)
from dbt_common.ui import warning_tag


# The classes in this file represent the data necessary to describe a
# particular event to both human readable logs, and machine reliable
# event streams. classes extend superclasses that indicate what
# destinations they are intended for, which mypy uses to enforce
# that the necessary methods are defined.


# Event codes have prefixes which follow this table
#
# | Code |     Description     |
# |:----:|:-------------------:|
# | A    | Pre-project loading |
# | D    | Deprecations        |
# | E    | DB adapter          |
# | I    | Project parsing     |
# | M    | Deps generation     |
# | P    | Artifacts           |
# | Q    | Node execution      |
# | W    | Node testing        |
# | Z    | Misc                |
# | T    | Test only           |
#
# The basic idea is that event codes roughly translate to the natural order of running a dbt task


# =======================================================
# D - Deprecations
# =======================================================


class BehaviorChangeEvent(WarnLevel):
    def code(self) -> str:
        return "D018"

    def message(self) -> str:
        return warning_tag(
            f"{self.description}\n"
            f"You may opt into the new behavior sooner by setting `flags.{self.flag_name}` to `True` in `dbt_project.yml`.\n"
            f"Visit {self.docs_url} for more information."
        )


# =======================================================
# M - Deps generation
# =======================================================


class RetryExternalCall(DebugLevel):
    def code(self) -> str:
        return "M020"

    def message(self) -> str:
        return f"Retrying external call. Attempt: {self.attempt} Max attempts: {self.max}"


class RecordRetryException(DebugLevel):
    def code(self) -> str:
        return "M021"

    def message(self) -> str:
        return f"External call exception: {self.exc}"


# =======================================================
# Z - Misc
# =======================================================


class SystemCouldNotWrite(DebugLevel):
    def code(self) -> str:
        return "Z005"

    def message(self) -> str:
        return (
            f"Could not write to path {self.path}({len(self.path)} characters): "
            f"{self.reason}\nexception: {self.exc}"
        )


class SystemExecutingCmd(DebugLevel):
    def code(self) -> str:
        return "Z006"

    def message(self) -> str:
        return f'Executing "{" ".join(self.cmd)}"'


class SystemStdOut(DebugLevel):
    def code(self) -> str:
        return "Z007"

    def message(self) -> str:
        return f'STDOUT: "{str(self.bmsg)}"'


class SystemStdErr(DebugLevel):
    def code(self) -> str:
        return "Z008"

    def message(self) -> str:
        return f'STDERR: "{str(self.bmsg)}"'


class SystemReportReturnCode(DebugLevel):
    def code(self) -> str:
        return "Z009"

    def message(self) -> str:
        return f"command return code={self.returncode}"


# We use events to create console output, but also think of them as a sequence of important and
# meaningful occurrences to be used for debugging and monitoring. The Formatting event helps eases
# the tension between these two goals by allowing empty lines, heading separators, and other
# formatting to be written to the console, while they can be ignored for other purposes. For
# general information that isn't simple formatting, the Note event should be used instead.


class Formatting(InfoLevel):
    def code(self) -> str:
        return "Z017"

    def message(self) -> str:
        return self.msg


class Note(InfoLevel):
    """Unstructured events.

    The Note event provides a way to log messages which aren't likely to be
    useful as more structured events. For console formatting text like empty
    lines and separator bars, use the Formatting event instead.
    """

    def code(self) -> str:
        return "Z050"

    def message(self) -> str:
        return self.msg


class PrintEvent(InfoLevel):
    # Use this event to skip any formatting and just print a message
    # This event will get to stdout even if the logger is set to ERROR
    # This is to support commands that want --quiet option but also log something to stdout
    def code(self) -> str:
        return "Z052"

    def message(self) -> str:
        return self.msg
