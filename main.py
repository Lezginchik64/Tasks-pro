# == Тип данных defaultdict ==
# Основная проблема при работе с обычными словарями (тип dict) – это попытка получить доступ (или изменить значение) по несуществующему ключу.
# Это приводит к возникновению ошибки KeyError.
# Мы уже научились решать данную проблему штатными способами, однако следует знать, что стандартная библиотека предоставляет тип данных defaultdict.

# Тип defaultdict ведет себя почти так же, как обычный словарь dict, но если мы попытаемся получить доступ (или изменить значение) по несуществующему ключу,
# то defaultdict автоматически создаст ключ и сгенерирует для него значение по умолчанию.
# Такое поведение делает defaultdict удобным вариантом обработки недостающих ключей в словарях.
# В приведенном ниже коде мы обращаемся к несуществующему ключу в словаре info:
# info = {'name': 'Timur', 'age': 29, 'job': 'Teacher'}
# print(info['salary'])   # ошибка

# Существует несколько способов избежать возникновения такой ошибки:
    # метод setdefault()
    # метод get()
    # проверка наличия ключа с помощью оператора принадлежности (key in dict)

# Следует отметить, что использование квадратных скобок (индексаторов) очень удобно и куда приятнее использования методов setdefault() и get().
# Для того чтобы не возникало ошибки при обращении по несуществующему ключу с помощью квадратных скобок, достаточно использовать альтернативный вариант словаря – defaultdict.
from collections import defaultdict

info = defaultdict(int)     # создаем словарь со значением по умолчанию 0
info['name'] = 'Timur'
info['age'] = 29
info['job'] = 'Teacher'
print(info['salary'])   # 0
print(info)             # defaultdict(<class 'int'>, {'name': 'Timur', 'age': 29, 'job': 'Teacher', 'salary': 0})

# Функция defaultdict() принимает в качестве аргумента тип элемента по умолчанию.
# Таким образом, для ключей, к которым происходит обращение, словарь defaultdict поставит в соответствие дефолтный элемент данного типа:
    # для int – число 0
    # для float – число 0.0
    # для bool – значение False
    # для str – пустая строка ''
    # для list – пустой список []
    # для tuple – пустой кортеж ()
    # для set – пустое множество set()
    # для dict – пустой словарь {}

# Помимо первого аргумента (типа элемента по умолчанию) мы можем передать второй аргумент – словарь, на основании которого будет создан defaultdict.
from collections import defaultdict
d = {'name': 'Timur', 'age': 29, 'job': 'Teacher'}
info = defaultdict(int, d)
print(info['name'])     # Timur
print(info['salary'])   # 0
print(info)             # defaultdict(<class 'int'>, {'name': 'Timur', 'age': 29, 'job': 'Teacher', 'salary': 0})

# Также допустимы все способы, которые мы используем при создании обычных словарей, а именно передача именованных аргументов или итерируемого объекта,
# содержащего пары ключ – значение (например, список кортежей).
from collections import defaultdict

info1 = defaultdict(int, name='Timur', age=29, job='Teacher')
info2 = defaultdict(int, [('name', 'Timur'), ('age', 29), ('job', 'Teacher')])
print(info1)    # defaultdict(<class 'int'>, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
print(info2)    # defaultdict(<class 'int'>, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})

# Обратите внимание, что при создании словаря defaultdict мы можем указать только именованные аргументы, но не можем указать только итерируемый объект с парами ключ – значение (или словарь).
info = defaultdict(name='Timur', age=29, job='Teacher')
print(info) # defaultdict(None, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
# а если так, то ошибка
info = defaultdict([('name', 'Timur'), ('age', 29), ('job', 'Teacher')])
print(info)     # ошибка
# приводит к возникновению ошибки, так как в качестве первого аргумента должен быть указан тип элемента по умолчанию, а не итерируемый объект с парами ключ – значение (или словарь).


# Рассмотрим задачу. Пусть задан список чисел numbers, в котором некоторые числа встречаются несколько раз.
# Нужно узнать, сколько именно раз встречается каждое из чисел.

# Решение 1. С помощью метода setdefault():
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:
    value = result.setdefault(num, 0)
    result[num] = value + 1

# Решение 2. С помощью метода get():
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1

# Решение 3. С помощью оператора принадлежности in:
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1

# Решение 4. С помощью типа данных defaultdict:
from collections import defaultdict
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
res = defaultdict(int)
for num in numbers:
    res[num] += 1
print(res)  # defaultdict(<class 'int'>, {9: 1, 8: 1, 32: 2, 1: 5, 10: 4, 23: 3, 4: 2, 2: 6})


# Тип данных defaultdict часто используют в связке с пустым списком в качестве значения по умолчанию, чтобы начинать добавление элементов без лишнего кода.
my_dict = defaultdict(list)
for i in range(7):
    my_dict[i].append(i)
print(my_dict)  # defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 6: [6]})
# При использовании defaultdict нет необходимости ни проверять наличие соответствующих ключей в словаре, ни создавать предварительно пустые списки.



# Когда использовать defaultdict?
# Приведем несколько рекомендаций, когда удобно использовать defaultdict вместо dict:
    # если ваш код в значительной степени основан на словарях и вы все время имеете дело с отсутствующими ключами
    # если элементы вашего словаря необходимо инициализировать некоторым значением по умолчанию
    # если ваш код использует словари для агрегирования, накопления, подсчета или группировки значений



# == Примечания ==
# Примечание 1. Тип defaultdict наследуется от типа dict.
from collections import defaultdict
print(issubclass(defaultdict, dict))    # True
# Таким образом, все методы, доступные для обычных словарей (тип dict), также доступны и для defaultdict-словарей.


# Примечание 2. Мы можем сравнивать обычные словари (тип dict) и defaultdict-словари.
info1 = {'name': 'Timur', 'age': 29, 'job': 'Teacher'}
info2 = defaultdict(int, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
print(info1 == info2)   # True


# Примечание 3. При создании defaultdict-словаря можно указывать не только тип данных для значений по умолчанию,
# но и любую функцию, не принимающую аргументов и возвращающую некоторое дефолтное значение.
# Приведенный ниже код (передаем функцию, объявленную с помощью def):
from collections import defaultdict

def get_default():
    return 69

info = defaultdict(get_default, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
print(info['name'])     # Timur
print(info['salary'])   # 69

#  Приведенный ниже код (передаем функцию, объявленную с помощью lambda):
info = defaultdict(lambda: '1000000$', {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
print(info['name'])     # Timur
print(info['salary'])   # 1000000$
# Обратите внимание, что передаваемая функция не должна принимать никаких аргументов.
def get_default(x):
    return 2 * x
info = defaultdict(get_default, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
print(info['name'])     # ошибка
print(info['salary'])   # ошибка
# приводит к возникновению ошибки.


# Примечание 4.
# Если создать экземпляр defaultdict-словаря без указания default_factory (значения по умолчанию для отсутствующих ключей),
# то поведение defaultdict будет таким же, как и у обычного словаря (тип dict).
data = defaultdict()
print(data['salary'])
# приводит к возникновению ошибки KeyError.
# Аналогичное поведение будет, если в качестве default_factory передать значение None.
data = defaultdict(None)
print(data['salary'])
# также приводит к возникновению ошибки KeyError.


# Примечание 5. Функцию, которая возвращает значение по умолчанию для отсутствующих ключей, можно явно менять через атрибут default_factory.
from collections import defaultdict

data = defaultdict(int)
print(data['salary1'])  # 0

data.default_factory = list
print(data['salary2'])  # []

data.default_factory = float
print(data['salary3'])  # 0.0

# Примечание 6. Тип defaultdict работает быстрее, чем использование методов setdefault() и get() обычного словаря (тип dict).

