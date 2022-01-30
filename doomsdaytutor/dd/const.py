from typing import List, Dict
from colorama import Fore, Style, init

WeekdayT = int
WeekdayDisplayT = str
StyleT = str

styleFor: Dict[str, StyleT] = {
    "control": Style.BRIGHT + Fore.YELLOW,
    "unknown_op": Fore.RED,
    "usage": Fore.BLUE,
    "section": Fore.BLUE,
    "data": Fore.BLACK + Style.DIM,
    "dataBright": Fore.WHITE + Style.DIM,
    "correct_msg": Style.BRIGHT + Fore.YELLOW,
    "incorrect_msg": Style.BRIGHT + Fore.RED,
}

weekdays: List[WeekdayT] = [
    # do not reorder
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]

# doomday in every month for easy calculation
leap_doomdays = [
    [  # isLeapYear == False
        (1, 3),
        (2, 28),
    ],
    [  # isLeapYear == True
        (1, 4),
        (2, 29),
    ],
]
doomdays = [
    # month, day
    # PI day
    (3, 14),
    # obvious
    (4, 4),
    (6, 6),
    (8, 8),
    (10, 10),
    (12, 12),
    # I work 9/5 at a 7/11.
    (5, 9),
    (9, 5),
    (7, 11),
    (11, 7),
]

# define date formatting in printing
locale = "de_DE"

# os agnostic terminal color
init()
