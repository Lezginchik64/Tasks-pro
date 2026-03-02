import json

with open('food_services.json', 'r', encoding='utf-8') as inp_file:
    reader = json.load(inp_file)

d, d2 = {}, {}
for i in reader:
    d[i['District']] = d.get(i['District'], 0) + 1
    if i['OperatingCompany'] == '':
        continue
    d2[i['OperatingCompany']] = d2.get(i['OperatingCompany'], 0) + 1

max_d = sorted(d.items(), key=lambda x: x[1], reverse=True)[0]  # max_d = max(d.items(), key=lambda x: x[1])
max_d2 = sorted(d2.items(), key=lambda x: x[1], reverse=True)[0]  # max_d = max(d, key=d.get)

print(f"{max_d[0]}: {max_d[1]}")
print(f"{max_d2[0]}: {max_d2[1]}")
