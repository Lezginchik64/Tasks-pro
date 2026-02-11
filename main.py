from datetime import datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]
# 1
data = [datetime.strptime(i[1], '%H:%M') - datetime.strptime(i[0], '%H:%M') for i in data]
print(sum(data, start=timedelta()).seconds // 60)

# 2
second = 0
for i in data:
    start, end = [datetime.strptime(x, '%H:%M') for x in i]
    second += (end - start).total_seconds()
print(int(second // 60))
