import csv

with open('data.csv', encoding="utf-8", newline='') as file_in:
    reader = csv.DictReader(file_in)
    d = {}
    for row in reader:
        domain = row['email'].split('@')[1]     # делаем домены из почты (было asda.asd@gmail.com, стало gmail.com)
        d[domain] = d.get(domain, 0) + 1    # добавляем домены (ключи) в словарь и считаем их количество (значения)
sorted_domains = sorted(d.items(), key=lambda x: (x[1], x[0]))

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['domain', 'count'])  # запись заголовков
    writer.writerows(sorted_domains)
