# write code that trains human to compute the doomsday algorithm
# georgian calendar
import datetime
from datetime import date
from typing import Iterable, Tuple, Generator

from .iox import stdio, p_factory, tcprint
from .const import (
    leap_doomdays,
    doomdays,
    weekdays,
    styleFor,
    WeekdayDisplayT,
    WeekdayT,
    locale,
)

from colorama import Style
from babel.dates import format_date


def print_calc_doomsday(date: date, io=stdio):
    p = p_factory(output=io.stdout)
    p(0, f"Doomsday of the year {date.year}", s="section")
    century_dd = print_calc_century_doomsday(date, io)
    conway_year_dd, rem_years = print_calc_conway_year_doomsday(date, io)
    weekday_offset = rem_years + rem_years // 4
    year_dd = (century_dd + conway_year_dd + weekday_offset) % 7

    p(
        2,
        f"For every remaining year, we need to add 1 day and 1 additional day for every leap year.",
    )
    p(2, f"{rem_years} + {rem_years // 4} = {weekday_offset}", s="dataBright")
    p(
        0,
        f"is equal to ({century_dd} + {conway_year_dd} + {weekday_offset}) mod 7 = {year_dd}",
        s="section",
    )

    assertCorrectness(datetime.date(date.year, 3, 14), year_dd)  # check with pi day

    # for within one year
    p(0, f"Weekday of {format_date(date, locale=locale)}", s="section")
    nearest_dd = nearest_doomsday(date)

    p(1, f"Choose known doomsday in that month: ", end="")
    p(0, format_date(nearest_dd, locale=locale), s="dataBright")

    wd = date_to_wd(nearest_dd)
    if nearest_dd != date:
        day_diff = date.day - nearest_dd.day
        wd = (year_dd + day_diff) % 7

        p(1, f"Calculate the difference in days: ", end="")
        p(0, f"{date.day} - {nearest_dd.day} = {day_diff}")
        p(1, "Add the difference to the known weekday and modulo 7:")
        p(2, f"({year_dd} + {day_diff}) mod 7 = {wd} = {weekdays[wd]}", s="dataBright")

    assertCorrectness(date, wd)
    p(0, f"is a {weekdays[wd]} ({wd}).", s="section")


def print_calc_century_doomsday(date: date, io=stdio) -> WeekdayT:
    tcprint(
        1,
        "Century: Recurring pattern of 5, 3, 2, 0 (Fri, Wed, Tue, Sun)",
        file=io.stdout,
    )
    century_doomsday = -1
    for century, doomsday, isCurrent in century_pattern(date):
        style = styleFor["data"]
        if isCurrent:
            century_doomsday = doomsday
            style = styleFor["dataBright"]
        tcprint(
            2,
            f"{century:4d} {weekday_to_str(doomsday):<9} {doomsday}",
            style=style,
            file=io.stdout,
        )  # TODO :>8 not safe for longer names
    return century_doomsday


# returns a generator of [century, doomsday, isCurrent]
def century_pattern(date_: date) -> Generator[int, WeekdayT, bool]:
    century_pattern = [5, 3, 2, 0]  # e. g. at 1800 1900 2000 2100
    cur_century = century_of(date_.year)
    dd = date(cur_century, 4, 4)  # known doomsday
    cur_weekday = date_to_wd(dd)
    cur_at = century_pattern.index(cur_weekday)

    base_century = cur_century - (100 * cur_at)
    for i in range(len(century_pattern)):
        century = base_century + 100 * i
        yield (century, century_pattern[i], century == cur_century)


def print_calc_conway_year_doomsday(date: date, io=stdio) -> Tuple[WeekdayT, int]:
    p = p_factory(output=io.stdout)
    wk, rest = conway_wd_rest(date)
    p(1, "Year: Recurring pattern of multiples of 12, starting from 0 (Conway)")
    for line in highlighted_conway_pattern(wk * 12):
        p(2, line)
    p(2, f"with the remaining ", end="")
    p(0, f"number of years = {rest}.", s="dataBright")
    return (wk, rest)


def conway_wd_rest(date: date) -> Tuple[WeekdayT, int]:
    decade = date.year - century_of(date.year)
    rest = decade % 12
    nearest_year = decade - rest
    return (int(nearest_year / 12), rest)


# returns lines to be printed.
def highlighted_conway_pattern(nearest_year: int) -> Tuple[str]:
    normalStyle = styleFor["data"]
    highlightedStyle = styleFor["dataBright"]

    def style(val, style_: str) -> str:
        return style_ + f"{val:>2}" + Style.RESET_ALL

    years = []
    wks = []
    for wk, year in enumerate(range(0, 100, 12)):
        yearStyle = normalStyle
        wkStyle = normalStyle
        if year == nearest_year:
            yearStyle = highlightedStyle
            wkStyle = highlightedStyle
        years.append(style(year, yearStyle))
        wks.append(style(wk, wkStyle))

    return ("  ".join(years), "  ".join(wks))


# nearest in the sense that it is in the same month, not nearest by day distance
def nearest_doomsday(date_: date) -> date:
    dd: Tuple[int, int] = None
    y = date_.year
    m = date_.month

    def f(seq: Iterable):
        return list(filter(lambda t: t[0] == m, seq))

    if m <= 2:
        # dependent on sequence point
        isLeapYear = (y % 400 == 0) or ((y % 100 != 0) and (y % 4 == 0))
        dd = f(leap_doomdays[int(isLeapYear)])[0]
    else:
        dd = f(doomdays)[0]
    return date(y, dd[0], dd[1])


def assertCorrectness(date: date, result: WeekdayT):
    assert date_to_wd(date) == result


def century_of(year: int) -> int:
    return int(year / 100) * 100


def wdd_to_wk(weekday: WeekdayDisplayT) -> WeekdayT:
    s = weekday.lower()
    return weekdays.index(s)


# convert datetime dates to weekday number
def date_to_wd(date: date) -> WeekdayT:
    # datetime uses monday = 0, tuesday = 1, ...
    wk = date.weekday()
    return (wk + 1) % 7


def weekday_to_str(weekday: WeekdayT) -> WeekdayDisplayT:
    assert 0 <= weekday <= 6
    return weekdays[weekday]


if __name__ == "__main__":
    today = date.today()
    print_calc_doomsday(today)
