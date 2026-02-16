from datetime import datetime as dt
import calendar

# 1
d = dt.strptime(input(), '%Y-%m-%d')
print(list(calendar.day_name)[d.weekday()])     # В разы быстрее 2 способа

# 2
print(dt.strptime(input(), '%Y-%m-%d').strftime('%A'))