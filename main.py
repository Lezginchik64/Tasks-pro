import csv

# 1
people = []
with open('titanic.csv', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        if int(row[0]) == 1 and float(row[3]) < 18:
            people.append(row)
people.sort(key=lambda x: x[2], reverse=True)
for i in people:
    print(i[1])

# 2
with open('titanic.csv', encoding='utf-8') as f:
    passengers = [d for s, *d, a in csv.reader(f, delimiter=';') if s == '1' and float(a) < 18]
    [print(name) for name, _ in sorted(passengers, key=lambda x: x[1], reverse=True)]
