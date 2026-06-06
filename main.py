f = input()
try:
    with open(f, 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print("Файл не найден")

# 2
try:
    file = open(f, 'r', encoding='utf-8')
    try:
        print(file.read())
    finally:
        file.close()
except FileNotFoundError:
    print("Файл не найден")
