from os import getenv as os_getenv
import sys
import textwrap
from typing import Dict

import colorama

# Colorama is needed for colored logs on Windows because we're using logger.info
# intead of print(). If the Windows env doesn't have a TERM var set or it is set to None
# (i.e. in the case of Git Bash on Windows- this emulates Unix), then it's safe to initialize
# Colorama with wrapping turned on which allows us to strip ANSI sequences from stdout.
# You can safely initialize Colorama for any OS and the coloring stays the same except
# when piped to another process for Linux and MacOS, then it loses the coloring. To combat
# that, we will just initialize Colorama when needed on Windows using a non-Unix terminal.

if sys.platform == "win32" and (not os_getenv("TERM") or os_getenv("TERM") == "None"):
    colorama.init(wrap=True)

COLORS: Dict[str, str] = {
    "red": colorama.Fore.RED,
    "green": colorama.Fore.GREEN,
    "yellow": colorama.Fore.YELLOW,
    "reset_all": colorama.Style.RESET_ALL,
}


COLOR_FG_RED = COLORS["red"]
COLOR_FG_GREEN = COLORS["green"]
COLOR_FG_YELLOW = COLORS["yellow"]
COLOR_RESET_ALL = COLORS["reset_all"]


USE_COLOR = True
PRINTER_WIDTH = 80


def color(text: str, color_code: str) -> str:
    if USE_COLOR:
        return "{}{}{}".format(color_code, text, COLOR_RESET_ALL)
    else:
        return text


def printer_width() -> int:
    return PRINTER_WIDTH


def green(text: str) -> str:
    return color(text, COLOR_FG_GREEN)


def yellow(text: str) -> str:
    return color(text, COLOR_FG_YELLOW)


def red(text: str) -> str:
    return color(text, COLOR_FG_RED)


def line_wrap_message(msg: str, subtract: int = 0, dedent: bool = True, prefix: str = "") -> str:
    """Line wrap a message to a given printer width.

    Line wrap the given message to PRINTER_WIDTH - {subtract}. Convert double
    newlines to newlines and avoid calling textwrap.fill() on them (like
    markdown)
    """
    width = printer_width() - subtract
    if dedent:
        msg = textwrap.dedent(msg)

    if prefix:
        msg = f"{prefix}{msg}"

    # If the input had an explicit double newline, we want to preserve that
    # (we'll turn it into a single line soon). Support windows, too.
    splitter = "\r\n\r\n" if "\r\n\r\n" in msg else "\n\n"
    chunks = msg.split(splitter)
    return "\n".join(textwrap.fill(chunk, width=width, break_on_hyphens=False) for chunk in chunks)


def warning_tag(msg: str) -> str:
    return f'[{yellow("WARNING")}]: {msg}'


def error_tag(msg: str) -> str:
    return f'[{red("ERROR")}]: {msg}'
