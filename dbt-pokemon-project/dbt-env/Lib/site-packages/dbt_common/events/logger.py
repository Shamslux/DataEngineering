import json
import logging
import threading
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from logging.handlers import RotatingFileHandler
from typing import Optional, TextIO, Any, Callable

from colorama import Style

from dbt_common.events.base_types import EventLevel, EventMsg
from dbt_common.events.format import timestamp_to_datetime_string
from dbt_common.utils.encoding import ForgivingJSONEncoder

PRINT_EVENT_NAME = "PrintEvent"


def _is_print_event(msg: EventMsg) -> bool:
    return msg.info.name == PRINT_EVENT_NAME


# A Filter is a function which takes a BaseEvent and returns True if the event
# should be logged, False otherwise.
Filter = Callable[[EventMsg], bool]


# Default filter which logs every event
def NoFilter(_: EventMsg) -> bool:
    return True


# A Scrubber removes secrets from an input string, returning a sanitized string.
Scrubber = Callable[[str], str]


# Provide a pass-through scrubber implementation, also used as a default
def NoScrubber(s: str) -> str:
    return s


class LineFormat(Enum):
    PlainText = 1
    DebugText = 2
    Json = 3


# Map from dbt event levels to python log levels
_log_level_map = {
    EventLevel.DEBUG: 10,
    EventLevel.TEST: 10,
    EventLevel.INFO: 20,
    EventLevel.WARN: 30,
    EventLevel.ERROR: 40,
}


# We need this function for now because the numeric log severity levels in
# Python do not match those for logbook, so we have to explicitly call the
# correct function by name.
def send_to_logger(logger, level: str, log_line: str):
    if level == "test":
        logger.debug(log_line)
    elif level == "debug":
        logger.debug(log_line)
    elif level == "info":
        logger.info(log_line)
    elif level == "warn":
        logger.warning(log_line)
    elif level == "error":
        logger.error(log_line)
    else:
        raise AssertionError(
            f"While attempting to log {log_line}, encountered the unhandled level: {level}"
        )


@dataclass
class LoggerConfig:
    name: str
    filter: Filter = NoFilter
    scrubber: Scrubber = NoScrubber
    line_format: LineFormat = LineFormat.PlainText
    level: EventLevel = EventLevel.WARN
    invocation_id: Optional[str] = None
    use_colors: bool = False
    output_stream: Optional[TextIO] = None
    output_file_name: Optional[str] = None
    output_file_max_bytes: Optional[int] = 10 * 1024 * 1024  # 10 mb
    logger: Optional[Any] = None


class _Logger:
    def __init__(self, config: LoggerConfig) -> None:
        self.name: str = config.name
        self.filter: Filter = config.filter
        self.scrubber: Scrubber = config.scrubber
        self.level: EventLevel = config.level
        self.invocation_id: Optional[str] = config.invocation_id
        self._python_logger: Optional[logging.Logger] = config.logger

        if config.output_stream is not None:
            stream_handler = logging.StreamHandler(config.output_stream)
            self._python_logger = self._get_python_log_for_handler(stream_handler)

        if config.output_file_name:
            file_handler = RotatingFileHandler(
                filename=str(config.output_file_name),
                encoding="utf8",
                maxBytes=config.output_file_max_bytes,  # type: ignore
                backupCount=5,
            )
            self._python_logger = self._get_python_log_for_handler(file_handler)

    def _get_python_log_for_handler(self, handler: logging.Handler):
        log = logging.getLogger(self.name)
        log.setLevel(_log_level_map[self.level])
        handler.setFormatter(logging.Formatter(fmt="%(message)s"))
        log.handlers.clear()
        log.propagate = False
        log.addHandler(handler)
        return log

    def create_line(self, msg: EventMsg) -> str:
        raise NotImplementedError()

    def write_line(self, msg: EventMsg):
        line = self.create_line(msg)
        if self._python_logger is not None:
            # We send PrintEvent to logger as error so it goes to stdout
            # when --quiet flag is set.
            # --quiet flag will filter out all events lower than ERROR.
            if _is_print_event(msg):
                level = "error"
            else:
                level = msg.info.level
            send_to_logger(self._python_logger, level, line)

    def flush(self):
        if self._python_logger is not None:
            for handler in self._python_logger.handlers:
                handler.flush()


class _TextLogger(_Logger):
    def __init__(self, config: LoggerConfig) -> None:
        super().__init__(config)
        self.use_colors = config.use_colors
        self.use_debug_format = config.line_format == LineFormat.DebugText

    def create_line(self, msg: EventMsg) -> str:
        return self.create_debug_line(msg) if self.use_debug_format else self.create_info_line(msg)

    def create_info_line(self, msg: EventMsg) -> str:
        scrubbed_msg: str = self.scrubber(msg.info.msg)  # type: ignore
        if _is_print_event(msg):
            # PrintEvent is a special case, we don't want to add a timestamp
            return scrubbed_msg
        ts: str = datetime.utcnow().strftime("%H:%M:%S")
        return f"{self._get_color_tag()}{ts}  {scrubbed_msg}"

    def create_debug_line(self, msg: EventMsg) -> str:
        log_line: str = ""
        # Create a separator if this is the beginning of an invocation
        # TODO: This is an ugly hack, get rid of it if we can
        ts: str = timestamp_to_datetime_string(msg.info.ts)
        if msg.info.name == "MainReportVersion":
            separator = 30 * "="
            log_line = f"\n\n{separator} {ts} | {self.invocation_id} {separator}\n"
        scrubbed_msg: str = self.scrubber(msg.info.msg)  # type: ignore
        level = msg.info.level
        log_line += (
            f"{self._get_color_tag()}{ts} [{level:<5}]{self._get_thread_name()} {scrubbed_msg}"
        )
        return log_line

    def _get_color_tag(self) -> str:
        return "" if not self.use_colors else Style.RESET_ALL

    def _get_thread_name(self) -> str:
        thread_name = ""
        if threading.current_thread().name:
            thread_name = threading.current_thread().name
            thread_name = thread_name[:10]
            thread_name = thread_name.ljust(10, " ")
            thread_name = f" [{thread_name}]:"
        return thread_name


class _JsonLogger(_Logger):
    def create_line(self, msg: EventMsg) -> str:
        from dbt_common.events.functions import msg_to_dict

        msg_dict = msg_to_dict(msg)
        raw_log_line = json.dumps(msg_dict, sort_keys=True, cls=ForgivingJSONEncoder)
        line = self.scrubber(raw_log_line)  # type: ignore
        return line
