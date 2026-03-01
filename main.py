import json
import csv

with open('students.json', 'r', encoding='utf-8') as inp_file:
    reader = json.load(inp_file)

d = {}
for i in reader:
    if i['age'] >= 18 and i['progress'] >= 75:
        d.setdefault(i['name'], i['phone'])
d = sorted(d.items(), key=lambda x: x[0])

with open('data.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'phone'])
    writer.writerows(d)
