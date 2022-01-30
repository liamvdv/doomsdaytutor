import sys
from typing import TextIO, Callable

from colorama import Style

from .const import StyleT, styleFor

# IO is an interface to allow easier testing
class IO:
    def __init__(
        self,
        stdin: TextIO = sys.stdin,
        stdout: TextIO = sys.stdout,
        stderr: TextIO = sys.stderr,
    ):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr


stdio = IO()

# tab color print, resets every time
def tcprint(tabs: int, *args, style="", **kwargs):
    kwargs["end"] = Style.RESET_ALL + kwargs.get("end", "\n")
    print("\t" * tabs + style + str(args[0]), *args[1:], **kwargs)


def p_factory(pretab=0, output=stdio.stdout) -> Callable:
    def p(tabs: int, *args, s: StyleT = "", **kwargs):
        tabs += pretab
        kwargs["file"] = output
        if s:
            s = styleFor[s]
        tcprint(tabs, *args, style=s, **kwargs)

    return p
