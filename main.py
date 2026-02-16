from datetime import datetime as dt
import calendar

d = dt.strptime(input(), '%Y %m')
print(calendar.monthrange(d.year, d.month)[1])