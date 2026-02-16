from datetime import datetime as dt
import calendar

# 1
year, month = input().split()
print(calendar.monthrange(int(year), list(calendar.month_name).index(month))[1])

# 2
d = dt.strptime(input(), '%Y %B')
print(calendar.monthrange(d.year, d.month)[1])
