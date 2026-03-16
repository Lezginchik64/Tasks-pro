from string import ascii_lowercase as abc

# 1
y = input()
translator = str.maketrans(abc, y)      # Метод str.maketrans() создаёт таблицу перевода символов.
print(input().translate(translator))    # Метод .translate() заменяет символы по таблице translator.
# То есть каждый символ из первой строки заменяется символом из второй строки по позиции.
# str.maketrans('', '', 'aeiou') - еще может удалять символы

# 2
d = {}
letters = input()
for i in range(len(abc)):
    d[abc[i]] = d.get(abc[i], letters[i])

for i in input().lower():
    print(d.get(i, i), end='')
# d.get(i, i) - возьми из словаря значение по ключу i, если ключа нет — верни сам i