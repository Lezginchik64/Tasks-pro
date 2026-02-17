from datetime import datetime
import calendar

year = int(input())
for month in range(1, 13):
    for day in range(15, 22):       # перебираем дни 15-21 и проверяем какой из них Четверг
        if calendar.weekday(year, month, day) == calendar.THURSDAY:
            thursday = datetime(year, month, day)
            print(thursday.strftime('%d.%m.%Y'))
            break
# первый четверг: 1-7
# второй четверг: 8-14
# третий: 15-21 - именно этот диапазон проверяется (середина месяца), в нем гарантировано будет Четверг