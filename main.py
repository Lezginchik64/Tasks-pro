import csv
from datetime import datetime

with open('name_log.csv', encoding='utf-8') as file:
    header, *rows = csv.reader(file)

d = {i[1]: i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(sorted(d.values(), key=lambda x: x[1]))
