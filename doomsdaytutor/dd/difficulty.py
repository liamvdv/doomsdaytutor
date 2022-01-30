from typing import Callable, Tuple
from datetime import MAXYEAR, MINYEAR, date, timedelta

today = date.today()


def timedelta_(*args, **kwargs) -> timedelta:
    years = kwargs.pop("years", 0)
    if years != 0:
        kwargs["weeks"] = kwargs.get("weeks", 0) + 52 * years

    return timedelta(*args, **kwargs)


def span_years(year: int, yearsPlus: int) -> Tuple[date, date]:
    start = today + timedelta_(years=year)
    end = today + timedelta_(years=yearsPlus)
    return (start, end)


difficulty_levels = [
    # start, end
    span_years(0, 1),
    span_years(-10, 11),
    span_years(-100, 101),
    span_years(-1000, 1001),
    (date(MINYEAR, 1, 1), date(MAXYEAR, 1, 1)),
]
NUM_LEVELS = len(difficulty_levels)


def atDifficulty(level=0) -> Tuple[date, date]:
    assert 0 <= level < len(difficulty_levels)
    return difficulty_levels[level]


if __name__ == "__main__":
    print(atDifficulty(0))
    print(atDifficulty(1))
    print(atDifficulty(2))
    print(atDifficulty(3))
    print(atDifficulty(4))

    def didErr(f: Callable, e):
        try:
            f()
        except e:
            return
        assert False, f"{f.__name__} did not raise {e.__name__}"

    didErr(lambda: print(atDifficulty(5)), AssertionError)
    didErr(lambda: print(atDifficulty(-1)), AssertionError)
