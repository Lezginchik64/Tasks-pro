import csv

# 1
with open('salary_data.csv', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    d = {}
    for i in reader:
        d.setdefault(i[0], []).append(int(i[1]))
    print(*sorted(d, key=lambda x: sum(d[x]) // len(d[x])), sep='\n')

# 2
with open('salary_data.csv', encoding="utf-8") as file:
    reader = list(csv.reader(file, delimiter=';'))
    d = {}
    for k, v in reader[1:]:
        d[k] = d.get(k, []) + [int(v)]
    print(*sorted(d, key=lambda x: sum(d[x]) // len(d[x])), sep='\n')
