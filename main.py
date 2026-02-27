import json

with open('data1.json', 'r', encoding='utf-8') as inp_file, open('data2.json', 'r', encoding='utf-8') as inp_file2:
    data1 = json.load(inp_file)
    data2 = json.load(inp_file2)

with open('data_merge.json', 'w', encoding='utf-8') as file:
    json.dump(data1 | data2, file, indent=3)
