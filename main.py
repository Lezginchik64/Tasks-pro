import json

with open('food_services.json', 'r', encoding='utf-8') as file:
    reader = json.load(file)

# 1
d = {}
for i in reader:
    d.setdefault(i['TypeObject'], []).append((i['Name'], i['SeatsCount']))

for i in sorted(d):
    max_place = max(d[i], key=lambda x: x[1])  # max_place = sorted(d[i], key=lambda x: x[1], reverse=True)[0]
    print(f"{i}: {max_place[0]}, {max_place[1]}")

# 2
d = {i['TypeObject']: f"{i['Name']}, {i['SeatsCount']}" for i in
     sorted(reader, key=lambda x: (x['TypeObject'], x['SeatsCount']))}
for i in d.items():
    print(f"{i[0]}: {i[1]}")
