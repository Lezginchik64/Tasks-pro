from datetime import timedelta, datetime as dt

# 1
start = dt.strptime(input(), '%d.%m.%Y')
end = dt.strptime(input(), '%d.%m.%Y')

while not (start.day + start.month) % 2:
    start += timedelta(days=1)

while start <= end:
    if start.isoweekday() != 4 and start.isoweekday() != 1:
        print(start.strftime('%d.%m.%Y'))
    start += timedelta(days=3)

# 2
start = dt.strptime(input(), '%d.%m.%Y')
end = dt.strptime(input(), '%d.%m.%Y')

current = start
while current <= end and (current.day + current.month) % 2 == 0:
    current = dt.fromordinal(current.toordinal() + 1)

while current <= end:
    if current.isoweekday() != 4 and current.isoweekday() != 1:
        print(current.strftime('%d.%m.%Y'))
    current = dt.fromordinal(current.toordinal() + 3)
