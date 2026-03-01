import json

with open('countries.json', 'r', encoding='utf-8') as inp_file:
    elements = json.load(inp_file)

res = {}
for elem in elements:
    res.setdefault(elem['religion'], []).append(elem['country'])

with open('religion.json', 'w', encoding='utf-8') as file:
    json.dump(res, file, indent=3)
