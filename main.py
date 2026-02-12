from datetime import datetime, timedelta

# 1
now = datetime.strptime(input(), '%d.%m.%Y %H:%M')
now_time = timedelta(hours=now.hour, minutes=now.minute)
if now.weekday() < 5 and timedelta(hours=9) <= now_time < timedelta(hours=21):
    print((timedelta(hours=21) - now_time).seconds // 60)
elif now.weekday() > 5 and timedelta(hours=10) <= now_time < timedelta(hours=18):
    print((timedelta(hours=18) - now_time).seconds // 60)
else:
    print("Магазин не работает")

# 2
now = datetime.strptime(input(), '%d.%m.%Y %H:%M')
now_time = timedelta(hours=now.hour, minutes=now.minute)
work_time = (timedelta(hours=9), timedelta(hours=21)) if now.weekday() in range(5) else (timedelta(hours=10),
                                                                                         timedelta(hours=18))
if now_time >= work_time[1] or now_time < work_time[0]:
    print("Магазин не работает")
else:
    print((work_time[1] - now_time).seconds // 60)
