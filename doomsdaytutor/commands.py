from .dd.iox import stdio
from .dd.tutor import play
from .dd.difficulty import atDifficulty
from .dd.feedback import p_factory

tldr = """Idea: Now the weekday of a date that is near the asked date.

Weekdays have numeric equivalent:
    Sun Mon Tue Wed Thu Fri Sat
    0   1   2   3   4   5   6

Some dates always share the same weekday within a year. They are called doomdays.
    (month / day)
     1/ 3 if not leap year, else 1/4
     2/28 if not leap year, else 2/29
     3/14
     4/ 4   6/ 6   8/ 8  10/10  12/12
     7/ 5   5/ 7  11/ 9   9/11
Mnemonic:  
    1/3 for three years, in the forth it's 1/4. Leap years matter.
    I work at a 7/5 from 9/11.
    3.14 is PI day.
    4/4 to 12/12 in 2s.

Centuries have a repeating pattern for these days: 5 3 2 0
    Year  Weekday  digit 
    1800  Fri      5 
    1900  Wed      3
    2000  Tue      2
    2100  Sun      0
    ...
The weekday shifts by one for every additional year, plus one additional for every leap year.
We can reduce the computation by floor division with 12, according to Conway:
    Year          :   0 12 24 36 48 60 72 84 96 
    Weekday offset:   0  1  2  3  4  5  6  7  8

This means the weekday of the doomsdays is:
    (century_weekday + conway_offset + rem_year + leap_years) mod 7
Then just pick the nearest doomsdate and impress your friends.
"""


def info(io=stdio, **kwargs):
    p = p_factory(0, output=io.stdout, default_s="control")
    p(
        0,
        "DOOMSDAYTUTOR - learn the doomsday algorithm",
    )
    p(0, "Watch https://www.youtube.com/watch?v=z2x3SSBVGJU or")
    p(0, tldr)
    p(0, "Unsure? Just start, false answers will be explained :D", s="incorrect_msg")


def level(io=stdio, **kwargs):
    lvl = kwargs.get("level", -1)
    assert lvl > -1, "invalid level input possible"
    off = play(*atDifficulty(lvl))
    return {"off": off}


def quit(io=stdio, **kwargs):
    stat(io, **kwargs)
    exit(0)


def stat(io=stdio, **kwargs):
    p = p_factory(0, default_s="control", output=io.stdout)
    rounds = kwargs.get("rounds", 0)
    correct = kwargs.get("correct_rounds", 0)
    if rounds > 0:
        perc = str(round(correct / rounds, 4) * 100) + "% accuracy"
    else:
        perc = ""
    p(
        0,
        f"You played {rounds} {'round' if rounds == 1 else 'rounds'} and got {correct} correct.",
        perc,
    )
