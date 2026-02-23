import csv

d = {}
with open('wifi.csv', encoding="utf-8") as file_in:
    reader = csv.DictReader(file_in, delimiter=';')
    for row in reader:
        reg = row['district']
        num = int(row['number_of_access_points'])
        d[reg] = d.get(reg, 0) + num
sorted_dict = sorted(d.items(), key=lambda x: (-x[1], x[0]))     # -x[1] - аналог реверса
print(*[f'{i[0]}: {i[1]}' for i in sorted_dict], sep='\n')
