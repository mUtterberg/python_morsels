import datetime


def meetup_date(year, month, nth=4, weekday=3):
    first_date = datetime.date(year, month, 1)
    day_of_week = first_date.weekday()
    day_diff = weekday - day_of_week
    if day_diff < 0:
        day_diff = day_diff + 7
    meeting_date = first_date + datetime.timedelta(days=day_diff, weeks=nth-1)
    return meeting_date
