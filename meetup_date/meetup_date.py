import datetime


def meetup_date(year, month):
    first_date = datetime.date(year, month, 1)
    thursday = 3
    day_of_week = first_date.weekday()
    if day_of_week < 3:
        day_diff = 3 - day_of_week
    elif day_of_week == 3:
        day_diff = 0
    else:
        day_diff = 3 - day_of_week + 7
    meeting_date = first_date + datetime.timedelta(days=day_diff, weeks=3)
    return meeting_date
