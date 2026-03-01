import json
import csv

d = {}
with open('playgrounds.csv', 'r', encoding='utf-8') as inp_file:
    reader = csv.DictReader(inp_file, delimiter=';')
    for i in reader:
        d.setdefault(i['AdmArea'], {}).setdefault(i['District'], []).append(i['Address'])

with open('addresses.json', 'w', encoding='utf-8') as file:
    json.dump(d, file, indent=3, ensure_ascii=False)
