from random import choice, randrange
from datetime import date, timedelta

import inquirer
from babel.dates import format_date

from .const import styleFor, weekdays, WeekdayT, locale
from .iox import stdio, tcprint
from .feedback import print_calc_doomsday, wdd_to_wk, date_to_wd

correct_msgs = ["Wow, well done!", "I'm impressed!"]
incorrect_msgs = [
    "Not quite! Let's take a look.",
    "Incorrect. Let's examine.",
]

# return value states how far off the guess was in days. [0, 6]
def play(start: date, end: date, io=stdio) -> int:  # TODO: pass stdin / out to inquirer
    date = random_date(start, end)
    want = date_to_wd(date)
    guess = prompt_weekday(date, io)
    isCorrect = guess == want
    print_encouragement(isCorrect, io)
    if not isCorrect:
        print_calc_doomsday(date, io)
    return want - guess


def random_date(start: date, end: date) -> date:
    assert start < end
    span = end - start
    delta_days = randrange(span.days)
    return start + timedelta(days=delta_days)


def prompt_weekday(date: date, io=stdio) -> WeekdayT:
    local_date = format_date(date, locale=locale)
    prompt = f"The {local_date} is a"
    capitalize = lambda s: s[0].upper() + s[1:]
    choices = list(map(capitalize, weekdays))
    try:
        result = inquirer.list_input(prompt, choices=choices)
    except KeyboardInterrupt:
        exit(0)
    # delete choices ? https://stackoverflow.com/questions/53980370/python-inquirer-module-remove-choices-when-done-using-curses
    return wdd_to_wk(result)


def print_encouragement(isCorrect: bool, io=stdio):
    color = ""
    msg = ""
    if isCorrect:
        msg = choice(correct_msgs)
        color = styleFor["correct_msg"]
    else:
        msg = choice(incorrect_msgs)
        color = styleFor["incorrect_msg"]
    tcprint(0, msg, style=color, file=io.stdout)
