from datetime import datetime as dt
import calendar

# 1
d = dt.strptime(input(), '%Y %b')
print(calendar.month(d.year, d.month))

# 2
year, month = input().split()
year, month = int(year), list(calendar.month_abbr).index(month)     # month_abbr - список с сокращенными названиями месяцев
calendar.prmonth(year, month)   # тоже самое, только работает без print