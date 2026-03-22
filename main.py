from collections import namedtuple
from datetime import datetime
import csv

# 1
with open('meetings.csv', 'r', encoding='utf-8') as file:
    header, *rows = csv.reader(file)
    Data = namedtuple('Data', header)
    sort_rows = sorted(rows, key=lambda x: datetime.strptime(f'{x[2]} {x[3]}', '%d.%m.%Y %H:%M'))
    for row in sort_rows:
        d = Data(*row)
        print(f'{d.surname} {d.name}')

    # можно функцией map
    for d in map(Data, sorted(rows, key=lambda x: datetime.strptime(f'{x[2]} {x[3]}', '%d.%m.%Y %H:%M'))):
        print(d.surname, d.name)

# 2
with open('meetings.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    Data = namedtuple('Data', reader.fieldnames)  # reader.fieldnames - первая строка (заголовки)
    for d in map(lambda r: Data(**r), sorted(reader,
                                             key=lambda x: datetime.strptime(f'{x['meeting_date']} {x['meeting_time']}',
                                                                             '%d.%m.%Y %H:%M'))):
        print(d.surname, d.name)
# ** распаковывает словарь в именованные аргументы
# ключи = имена параметров
# значения = передаваемые данные