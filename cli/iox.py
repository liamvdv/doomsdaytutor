import sys
from typing import TextIO

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
