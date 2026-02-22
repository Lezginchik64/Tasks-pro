import csv

with open('deniro.csv', encoding="utf-8") as file:
    reader = list(csv.reader(file))
    n = int(input()) - 1
    reader_sorted = sorted(reader, key=lambda x: int(x[n]) if x[n].isdigit() else x[n])
    for i in reader_sorted:
        print(*i, sep=',')