from datetime import datetime, timedelta

dt = datetime.strptime(input(), '%d.%m.%Y')
print(dt.strftime('%d.%m.%Y'))
for i in range(2, 11):
    dt += timedelta(days=i)
    print(dt.strftime('%d.%m.%Y'))
