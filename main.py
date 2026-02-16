from datetime import date
import calendar


# 1
def get_days_in_month(year, month):
    month_num = list(calendar.month_name).index(month)
    return [date(year, month_num, day) for day in range(1, calendar.monthrange(year, month_num)[1] + 1)]


# 2
def get_days_in_month(year, month):
    month_num = list(calendar.month_name).index(month)
    count_day = calendar.monthrange(year, month_num)[1]
    start = date(year, month_num, 1).toordinal()
    end = date(year, month_num, count_day).toordinal()
    return sorted([date.fromordinal(i) for i in range(start, end + 1)])


print(get_days_in_month(2021, 'December'))
