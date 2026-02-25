import csv

with open('student_counts.csv', 'r', encoding='utf-8') as f1, open('sorted_student_counts.csv', 'w',
                                                                   encoding='utf-8') as f2:
    reader = csv.reader(f1)
    writer = csv.writer(f2)

    classes = list(zip(*reader))    # транспонирование
    colomn = classes[0]
    del classes[0]
    sort_classes = sorted(classes, key=lambda x: ([int(x[0].split('-')[0])], [x[0].split('-')[1]]))
    sort_classes.insert(0, colomn)
    writer.writerows(list(zip(*sort_classes)))  # транспонирование обратно

# Переворачиваем таблицу (чтобы сортировать столбцы)
# Сортируем классы по номеру и букве
# Переворачиваем обратно
# Записываем