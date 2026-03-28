# == Тип данных OrderedDict ==
# Тип OrderedDict является подтипом типа dict, сохраняющим порядок, в котором пары ключ — значение вставляются в словарь.
# Когда мы перебираем объект типа OrderedDict, его элементы перебираются в исходном порядке.
# Если мы обновим значение существующего ключа, то порядок останется неизменным.
# Если мы удалим элемент и вставим его снова, то этот элемент будет добавлен в конец словаря.

# Тип OrderedDict, будучи подтипом dict, наследует все методы, предоставляемые обычным словарем.
# При этом в OrderedDict также есть дополнительные методы, о которых мы поговорим ниже.
# В отличие от dict, тип OrderedDict не является встроенным типом, и для использования его необходимо импортировать из модуля collections.
from collections import OrderedDict

numbers = OrderedDict()
numbers['one'] = 1
numbers['two'] = 2
numbers['three'] = 3
print(numbers)  # OrderedDict({'one': 1, 'two': 2, 'three': 3})

# Как обычные словари или defaultdict, эти словари можно создавать любым из доступных способов:
numbers1 = OrderedDict({'one': 1, 'two': 2, 'three': 3})
numbers2 = OrderedDict([('one', 1), ('two', 2), ('three', 3)])
numbers3 = OrderedDict(one=1, two=2, three=3)




# == Изменение словаря OrderedDict ==
# Тип OrderedDict является изменяемым. Мы можем вставлять новые элементы, обновлять и удалять существующие элементы.
# Если мы вставим новый элемент в существующий OrderedDict-словарь, то этот элемент добавится в конец словаря.
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)      # OrderedDict({'one': 1, 'two': 2, 'three': 3})
numbers['four'] = 4
print(numbers)      # OrderedDict({'one': 1, 'two': 2, 'three': 3, 'four': 4})

# Если мы удалим элемент из существующего OrderedDict-словаря и снова вставим его, то он будет помещен в конец словаря.
numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)    # OrderedDict({'one': 1, 'two': 2, 'three': 3})
del numbers['one']
print(numbers)    # OrderedDict({'two': 2, 'three': 3})
numbers['one'] = 1
print(numbers)  # OrderedDict({'two': 2, 'three': 3, 'one': 1})

# Если мы обновляем значение по существующему ключу, то ключ сохраняет свою позицию.
numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)      # OrderedDict({'one': 1, 'two': 2, 'three': 3})
numbers['one'] = 1.0
print(numbers)      # OrderedDict({'one': 1.0, 'two': 2, 'three': 3})
numbers.update(two=2.0) # обновляем значение по существующему ключу
print(numbers)      # OrderedDict({'one': 1.0, 'two': 2.0, 'three': 3})
# Обновить значение по нужному ключу можно либо с помощью квадратных скобок, либо с помощью словарного метода update().



# == Итерирование по словарю OrderedDict ==
# Доступ к элементам и итерирование по OrderedDict-словарям работает так же, как и у обычных словарей.
# Мы можем перебирать ключи напрямую или с использованием словарных методов items(), keys() и values().
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
    # обращение по ключу
print(numbers['one'])   # 1
print(numbers['three']) # 3
# перебор ключей напрямую
for key in numbers:
    print(key, '->', numbers[key])
# one -> 1
# two -> 2
# three -> 3
    # перебор пар (ключ, значение) через метод
for key, value in numbers.items():
    print(key, '->', value)
# one -> 1
# two -> 2
# three -> 3
    # перебор ключей через метод
for key in numbers.keys():
    print(key, '->', numbers[key])
# one -> 1
# two -> 2
# three -> 3
    # перебор значений через метод
for value in numbers.values():
    print(value)
# 1
# 2
# 3

# При итерировании по OrderedDict-словарям мы можем использовать встроенную функцию reversed().
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
    # перебор ключей напрямую
for key in reversed(numbers):
    print(key, '->', numbers[key])
# three -> 3
# two -> 2
# one -> 1
    # перебор пар (ключ, значение) через метод
for key, value in reversed(numbers.items()):
    print(key, '->', value)
# three -> 3
# two -> 2
# one -> 1
# Начиная с Python 3.8 обычные словари (тип dict) также поддерживают использование встроенной функции reversed().




# == Методы popitem() и move_to_end() ==
# OrderedDict-словари имеют два полезных метода:
    # метод move_to_end() позволяет переместить существующий элемент либо в конец, либо в начало словаря
    # метод popitem() позволяет удалить и вернуть элемент либо из конца, либо из начала словаря


# -- Метод move_to_end() --
# Методу move_to_end() можно передать два аргумента:
    # key (обязательный аргумент) – ключ, который идентифицирует перемещаемый элемент
    # last (необязательный аргумент) – логическое значение (тип bool), которое определяет, в какой конец словаря мы перемещаем элемент:
        # значение True (по умолчанию) перемещает элемент в конец, значение False – в начало
# Если при вызове метода move_to_end() переданный ключ отсутствует в словаре, то возникает ошибка KeyError.
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)  # OrderedDict({'one': 1, 'two': 2, 'three': 3})
numbers.move_to_end('one')  # last=True
print(numbers)  # OrderedDict({'two': 2, 'three': 3, 'one': 1})
numbers.move_to_end('three', last=False)    # last=False
print(numbers)  # OrderedDict({'three': 3, 'two': 2, 'one': 1})

# С помощью метода move_to_end() мы можем сортировать OrderedDict-словарь по ключам.
letters = OrderedDict(b=2, d=4, a=1, c=3)
for key in sorted(letters):
    letters.move_to_end(key)
print(letters)  # OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})


# -- Метод popitem() --
# Метод popitem() по умолчанию удаляет и возвращает элемент в порядке LIFO (Last-In/First-Out, последний пришел/первый ушел).
# Другими словами, метод popitem() удаляет элементы с конца словаря.
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers.popitem())    # ('three', 3)
print(numbers)  # OrderedDict({'one': 1, 'two': 2})
print(numbers.popitem())    # ('two', 2)
print(numbers)  # OrderedDict({'one': 1})

# Если методу popitem() передать необязательный аргумент last=False,
# то он начнет удалять и возвращать элементы в порядке FIFO (First-In/First-Out, первый пришел/первый ушел).
numbers = OrderedDict(one=1, two=2, three=3)
print(numbers.popitem(last=False))  # ('one', 1)
print(numbers)  # OrderedDict({'two': 2, 'three': 3})
print(numbers.popitem(last=False))  # ('two', 2)
print(numbers)  # OrderedDict({'three': 3})



# == Сравнение словарей ==
# При сравнении на равенство обычных словарей (тип dict) порядок расположения их элементов неважен.
letters1 = dict(a=1, b=2, c=3, d=4)
letters2 = {'b': 2, 'a': 1, 'c': 3, 'd': 4}
letters3 = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(letters1 == letters2)     # True
print(letters1 == letters3)     # True

# При сравнение на равенство OrderedDict-словарей порядок расположения их элементов важен.
letters1 = OrderedDict(a=1, b=2, c=3, d=4)
letters2 = OrderedDict({'b': 2, 'a': 1, 'c': 3, 'd': 4})
letters3 = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(letters1 == letters2)     # False
print(letters1 == letters3)     # True

# При сравнении на равенство обычного словаря (тип dict) и OrderedDict-словаря порядок расположения их элементов неважен.
letters1 = OrderedDict(a=1, b=2, c=3, d=4)
letters2 = {'b': 2, 'a': 1, 'c': 3, 'd': 4}
print(letters1 == letters2)     # True



# == Примечания ==
# Примечание 4. Мы можем использовать метод fromkeys() для создания OrderedDict-словарей.
from collections import OrderedDict

keys = ['one', 'two', 'three']
numbers = OrderedDict.fromkeys(keys, 0)
print(numbers)  # OrderedDict({'one': 0, 'two': 0, 'three': 0})

# Примечание 5. В Python 3.9 появились операторы | и |=, которые реализуют операцию конкатенации словарей — как обычных, так и OrderedDict.
physicists = OrderedDict(newton='1642-1726', einstein='1879-1955')
biologists = OrderedDict(darwin='1809-1882', mendel='1822-1884')
scientists = physicists | biologists
print(scientists)  # OrderedDict({'newton': '1642-1726', 'einstein': '1879-1955', 'darwin': '1809-1882', 'mendel': '1822-1884'})

physicists = OrderedDict(newton='1642-1726', einstein='1879-1955')
physicists1 = OrderedDict(newton='1642-1726/1727', hawking='1942-2018')
physicists |= physicists1
print(physicists)   # OrderedDict({'newton': '1642-1726/1727', 'einstein': '1879-1955', 'hawking': '1942-2018'})