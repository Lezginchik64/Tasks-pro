import json

with open('people.json', 'r', encoding='utf-8') as inp_file:
    elements = json.load(inp_file)

all_keys = set()  # для сбора всех возможных ключей
for elem in elements:
    all_keys.update(elem.keys())

for elem in elements:
    for i in all_keys:
        elem[i] = elem.get(i, None)

with open('updated_people.json', 'w', encoding='utf-8') as file:
    json.dump(elements, file, indent=3)
