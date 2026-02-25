import csv

def clss_sort_key(class_name):              # Функция преобразования из 5-Б в (5, Б) причем 5 - становится числом
    number, letter = class_name.split('-')
    return (int(number), letter)


with open('student_counts.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    columns = ['year'] + sorted(reader.fieldnames[1:], key=clss_sort_key)   # прибавляем колонку "Год" + сортируем список классов
    rows = list(reader)     # Исходный не отсортированный список

# Метод reader.fieldnames() позволяет сразу извлечь все заголовки из файла, он возвращает отдельный объект-список,
# итерирования по итератору не происходит, итерирование происходит именно по списку.

with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)


# data = {'a': 1, 'b': 2, 'c': 3}

# with open('data.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=['c', 'b', 'a'])
#     writer.writeheader()
#     writer.writerow(data)

# создаст файл data.csv с содержанием:
# c,b,a
# 3,2,1