import inquirer
from typing import Tuple

from .dd.difficulty import NUM_LEVELS
from .dd.iox import stdio
from .dd.feedback import p_factory

from .commands import level, quit, stat, info

commands = {
    "quit": quit,
    "q": quit,
    "info": info,
    "i": info,
    "stat": stat,
    "s": stat,
    "": level,
    # digits: level
}

usage_text = """Usage: python doomsdaytutor
    <digit>   := play level <digit>; 0 is 'easy', 5 is very hard
    [enter]   := play current level again
    i := info := information on doomsday algorithm
    s := stat := statistics about current session
    q := quit := quit the program
"""


def usage(io=stdio, **kwargs):
    p_factory(output=io.stdout)(0, usage_text, s="usage")

def propose_usage(io=stdio, **kwargs):
    op = kwargs.get("raw_op", "")
    msg = f"unknown command '{op}', q to leave"
    p_factory(output=io.stdout)(0, msg, s="unknown_op")

def run(io=stdio):
    ctx = {"level": 0, "rounds": 0, "correct_rounds": 0}
    usage(io)
    while True:
        op = nextOp(io)
        ctx["raw_op"] = op
        
        cmd = commands.get(op, None)
        if cmd is None:
            lvl, isLevel = isLevelOp(op)
            if isLevel:
                cmd = commands.get("")
                ctx["level"] = lvl
            else:
                cmd = propose_usage

        ret = cmd(io, **ctx)
        if cmd == level:
            ctx["rounds"] += 1
            ctx["correct_rounds"] += ret["off"] == 0


def nextOp(io=stdio) -> str:
    io.start_middleman_sysstdio()
    try:
        text = inquirer.text(message="(op)")
    except KeyboardInterrupt:
        return "quit"
    finally:
        io.stop_middleman_sysstdio()
    return text


def isLevelOp(op: str) -> Tuple[int, bool]:
    n, ok = toInt(op)
    return n, ok and (0 <= n < NUM_LEVELS)


def toInt(s: str) -> Tuple[int, bool]:
    try:
        n = int(s)
    except ValueError:
        return -1, False
    return n, True
