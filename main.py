import csv

# 1
def csv_columns(filename):

    with open(filename, encoding="utf-8") as file_in:
        rows = list(csv.reader(file_in))
        return {key: value for key, *value in zip(*rows)}

# 2
def csv_columns(filename):
    res = {}
    with open(filename, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for column, value in row.items():
                res.setdefault(column, []).append(value)
    return res


text = '''name,grade
Timur,5
Arthur,4
Anri,5'''

with open('grades.csv', 'w') as file:
    file.write(text)

print(csv_columns('grades.csv'))
