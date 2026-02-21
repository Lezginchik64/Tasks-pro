import csv

# 1
with open('sales.csv', encoding='utf-8', newline='') as file:
    # file.readline() так можно пропустить первую строку
    rows = csv.reader(file, delimiter=';')
    next(rows)  # пропуск первой строки
    for row in rows:
        if int(row[1]) > int(row[2]):
            print(row[0])

# 2
with open('sales.csv', encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        if int(row['new_price']) < int(row['old_price']):
            print(row['name'])