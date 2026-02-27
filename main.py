import json

1
with open('data.json', 'r', encoding='utf-8') as inp_file:
    elements = json.load(inp_file)

res = []
for elem in elements:
    if isinstance(elem, str):
        res.append(elem + '!')
    elif isinstance(elem, bool):
        res.append(not elem)
    elif isinstance(elem, int):
        res.append(elem + 1)
    elif isinstance(elem, list):
        res.append(elem * 2)
    elif isinstance(elem, dict):
        elem['newkey'] = None
        res.append(elem)

with open('updated_data.json', 'w', encoding='utf-8') as file:
    json.dump(res, file, indent=3)


# 2
with open('data.json', encoding='utf-8') as file, open('updated_data.json', 'w', encoding='utf-8') as new_file:
    data_json = json.load(file)
    conv_values = {
        str: lambda x: x + '!',
        int: lambda x: x + 1,
        bool: lambda x: not x,
        list: lambda x: x * 2,
        dict: lambda x: {**x, 'newkey': None}
    }
    new_data = []
    for i in data_json:
        if type(i) in conv_values:
            new_data.append(conv_values[type(i)](i))
    json.dump(new_data, new_file, indent=2)
