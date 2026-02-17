from datetime import datetime, timedelta, date
import calendar


# 1
def get_all_mondays(year):
    mondays = []
    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            monday = week[0]
            if monday:
                mondays.append(date(year, month, monday))
    return mondays


# # 2
def get_all_mondays(year):
    res = []
    start = datetime(year, 1, 1)
    while start.year == year:
        if start.weekday() == 0:
            res.append(start)
        start += timedelta(days=1)
    return [i.date() for i in res]


print(get_all_mondays(2021))
