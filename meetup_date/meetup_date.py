import datetime
from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=3):
    if nth < 0:
        border_date = datetime.date(year, month+1, 1) - datetime.timedelta(days=1)
        day_of_week = border_date.weekday()
        day_diff = day_of_week - weekday
        if day_diff < 0:
            day_diff = day_diff + 7
        meeting_date = border_date - datetime.timedelta(days=day_diff, weeks=-nth-1)
    else:
        border_date = datetime.date(year, month, 1)
        day_of_week = border_date.weekday()
        day_diff = weekday - day_of_week
        if day_diff < 0:
            day_diff = day_diff + 7
        meeting_date = border_date + datetime.timedelta(days=day_diff, weeks=nth-1)
    return meeting_date
