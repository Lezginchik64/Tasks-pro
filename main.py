# == Тип данных namedtuple. Часть 1 ==

# == Модуль collections ==
# Python содержит встроенный модуль collections, который содержит специализированные типы коллекций, альтернативных традиционным list, tuple, dict:
    # namedtuple
    # defaultdict
    # OrderedDict
    # Counter
    # ChainMap
    # deque
# В рамках данного урока мы изучим именованные кортежи (тип namedtuple).


# == Именованные кортежи ==
# Именованные кортежи (тип namedtuple) — это подтип обычных кортежей в Python.
# У них те же функции, что и у обычных, но их значения можно получать как с помощью индекса (например, [0]), так и с помощью имени через точку (например, .name).
# Основное предназначение именованных кортежей — улучшение читаемости программного кода.
# Не забывайте, что кортежи являются неизменяемыми. При попытке изменить значение кортежа мы получим ошибку TypeError.

# Рассмотрим пример, в котором происходит работа с точкой на плоскости, имеющей две координаты x и y.
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])     # объявляем тип Point именованного кортежа
point = Point(3, 7)                         # создаем именованный кортеж Point
print(point)         # Point(x=3, y=7)
print(point.x, point.y)     # 3 7
print(point[0], point[1])   # 3 7
print(type(point))      # <class '__main__.Point'>
# В приведенном выше коде мы создали объект типа Point, который является именованным кортежем.
# Обратиться к полям именованного кортежа можно через точку (point.x, point.y) или по индексу (point[0], point[1]), как и в обычных кортежах.

# Важно отметить, что, хотя кортежи и именованные кортежи неизменяемы, сохраняемые в них значения не обязательно должны быть неизменяемыми.
# Совершенно законно создать кортеж или именованный кортеж, содержащий изменяемые значения.
from collections import namedtuple

Person = namedtuple('Persons', ['name', 'children', 'dog'])
# Persons - это название кортежа, ['name', 'children', 'dog'] - это элементы кортежа

sveta = Person('Sveta Gueva' , ['Larisa', 'Timur'], 'bob')
# 'name' - 'Sveta Gueva', 'children' - ['Larisa', 'Timur'], 'dog' - 'bob'

print(sveta)       # Persons(name='Sveta Gueva', children=['Larisa', 'Timur'], dog='bob')
sveta.children.append('Soslan')
print(sveta)       # Person(name='Sveta Gueva', children=['Larisa', 'Timur', 'Soslan'])
# Таким образом, мы можем создавать именованные кортежи, содержащие изменяемые объекты. Мы можем изменять изменяемые объекты в исходном кортеже.
# Однако это не означает, что мы изменяем сам кортеж. Кортеж продолжит содержать те же ссылки на память.

# Кортежи и именованные кортежи с изменяемыми значениями не могут быть хешированы, поэтому не могут быть элементами множеств и ключами в словарях.
# Кортежи и именованные кортежи без изменяемых значений могут быть хешированы, поэтому могут быть элементами множеств и ключами в словарях.




# == Функция namedtuple() ==
# Функция namedtuple() выступает в роли фабричной функции, порождающей новые типы данных.
# Сигнатура данной функции имеет следующий вид:
    # namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
# То есть функция принимает два обязательных параметра typename и field_names и три необязательных rename, defaults, module, имеющих значения по умолчанию False, None, None.


# -- Параметры typename и field_names --
# Параметр typename отвечает за имя создаваемого типа, параметр field_names — за названия полей.
# Имя типа — это строка с типом, который нужно сделать именованным кортежем.
# В качестве параметра field_names могут быть использованы:
    # список
    # словарь
    # кортеж
    # строка
    # множество

# Параметр field_names является списком:
Point = namedtuple('Point', ['x', 'y'])    # в качестве второго параметра передаем список
point =  Point(2, 4)
print(point)    # выводит Point(x=2, y=4)

# Параметр field_names является кортежем:
Point = namedtuple('Point', ('x', 'y'))    # в качестве второго параметра передаем кортеж
point =  Point(2, 4)
print(point)    # выводит Point(x=2, y=4)

# Параметр field_names является словарем:
# В этом случае для полей именованного кортежа используются ключи словаря, поэтому в качестве значений можно указать все что угодно.
Point = namedtuple('Point', {'x': 0, 'y': 69})  # в качестве второго параметра передаем словарь
point = Person(2, 4)
print(point)    # # выводит Point(x=2, y=4)

# Параметр field_names является строкой:
# При создании именованного кортежа с помощью строки мы указываем поля либо через символ пробела, либо разделяя их символом ,
Point = namedtuple('Point', 'x y')    # в качестве второго параметра передаем строку
# либо так: Point = namedtuple('Point', 'x,y')     # в качестве второго параметра передаем строку
point =  Point(2, 4)
print(point)                          # выводит Point(x=2, y=4)

# Параметр field_names является множеством:
# Мы можем создать именованный кортеж с помощью множества, однако делать это не рекомендуется.
# Как мы знаем, множество – это неупорядоченный набор данных.
# Когда мы используем неупорядоченный набор данных для предоставления полей именованному кортежу, мы можем получить неожиданный результат.
Point = namedtuple('Point', {'x', 'y'})    # в качестве второго параметра передаем множество
point =  Point(2, 4)
print(point)    # может быть как: Point(x=2, y=4) или так : Point(y=2, x=4)

# В качестве параметра field_names можно передавать любой итерируемый объект, например, результат вызова функций map() и filter().

# Обратите также внимание на то, что создавать именованные кортежи можно не только с помощью позиционных аргументов, но и с помощью именованных.
Point = namedtuple('Point', ['x', 'y'])
point1 = Point(2, 4)                          # позиционные аргументы
point2 = Point(y=10, x=3)                     # именованные аргументы
print(point1)   # Point(x=2, y=4)
print(point2)   # Point(x=3, y=10)

# В качестве названия полей для именованных кортежей мы можем использовать любое корректное название имени переменной за исключением:
    # имен, начинающихся с подчеркивания (_)
    # ключевых слов языка Python (if, with, else, class, ...)


# -- Параметр rename --
# Допустим, мы импортируем данные из CSV-файла и превращаем каждую строку в именованный кортеж. Структура файла имеет вид:
    # name,surname,age,class
    # Timur,Guev,28,11
    # Ruslan,Chaniev,22,9
    # ...
# Названия полей мы берем из заголовка CSV-файла:
headers = ('name', 'surname', 'age', 'class')
Student = namedtuple('Student', headers)
# Поскольку одно поле имеет название class (ключевое слово языка Python), мы получаем ошибку: ValueError: Type names and field names cannot be a keyword: 'class'.
# Проблема заключается в том, что мы не знаем, будут ли у нас в качестве названий полей ключевые слова языка Python или нет.
# Для решения данной проблемы можно использовать параметр rename со значением True.
Students = namedtuple('Student', headers, rename=True)
stud = Students('Роман', 'Белых', 26, 10)
print(stud)     # Student(name='Роман', surname='Белых', age=26, _3=10)
# Обратите внимание на то, что Python автоматически переименовал поле class в _3.

headers = ('name', 'surname', 'age', 'class', 'with', 'color', 'name', 'class', 'if')
Student = namedtuple('Student', headers, rename=True)
stud = Student('Тимур', 'Гуев', 28, 11, 'sister', 'green', 'Tim', '11A', 'else')
print(stud)     # Student(name='Тимур', surname='Гуев', age=28, _3=11, _4='sister', color='green', _6='Tim', _7='11A', _8='else')
# Как мы видим, неудачные имена полей переименовались в соответствии с их порядковыми номерами, причем перед порядковым номером используется символ подчеркивания.


# -- Параметр defaults --
# Параметр defaults используется для того, чтобы установить значения по умолчанию для полей именованного кортежа.
Point = namedtuple('Point', ['x', 'y'], defaults=(0, 0))
point1 = Point()
point2 = Point(1, 9)
print(point1)   # Point(x=0, y=0)
print(point2)   # Point(x=1, y=9)
# Можно указать значение по умолчанию только для некоторых полей, при этом defaults присваивает значения по умолчанию с конца.
Point = namedtuple('Point', ['x', 'y'], defaults=(0,))
point =  Point(7)      # используем значения по умолчанию для y
print(point)    # Point(x=7, y=0)


# -- Параметр module --
Point = namedtuple('Point', ['x', 'y'])
point = Point(1, 2)
print(type(point))  # <class '__main__.Point'>
# Если мы укажем допустимое имя модуля для этого аргумента, тогда атрибуту .__ module__ результирующего именованного кортежа будет присвоено это значение.
Point = namedtuple('Point', ['x', 'y'], module='customtypes')
point = Point(1, 2)
print(type(point))  # <class 'customtypes.Point'>
# Параметр module был добавлен в Python 3.6 для того, чтобы появилась возможность сериализовать/десериализовать именованные кортежи с помощью модуля pickle в разных реализациях Python (IronPython, Jython и так далее).



# == Распаковка именованного кортежа ==
# Мы можем распаковывать именованный кортеж так же, как и обычный.
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])
timur = Person('Timur', 29, 170)
name, age, height = timur
print(name)     # Тимур
print(age)      # 29
print(height)   # 170


# Примечание 5. При работе с именованным кортежами мы можем использовать срезы.
Point = namedtuple('Point3D', ['x', 'y', 'z'])
point = Point(89, 13, 22)
print(point[1:])    # (13, 22)
print(point[:2])    # (89, 13)
print(point[1:2])    # (13,)
# Обратите внимание на то, что результатом среза является обычный кортеж (тип данных tuple).

# Примечание 7. Именованные кортежи (тип namedtuple) являются производными от обычных кортежей (тип tuple), поэтому наследуют все их методы.


# Из csv мы можем создать коллекцию экземпляров типа 'Point'.
# Например, у нас есть  файл points.csv, в котором два столбца — координаты х и y соответственно.
# Тогда мы можем проитерироваться по этому файлу, создавая экземпляры типа 'Point' и добавляя их в какой-либо список:
import csv
import random
from collections import namedtuple

Point = namedtuple('Point', ('x', 'y'))

with open('points.csv', mode='w', encoding='utf-8') as file_out:
    data = [[random.randint(0, 100), random.randint(0, 100)] for _ in range(20)]
    writer = csv.writer(file_out)
    writer.writerows(data)

with open('points.csv', mode='r', encoding='utf-8') as file_in:
    rows = csv.reader(file_in)
    points = []
    for row in rows:
        x, y = row
        points.append(Point(int(x), int(y)))
print(points)
# [Point(x=67, y=33), Point(x=98, y=72), Point(x=54, y=44), Point(x=12, y=78), Point(x=99, y=97), Point(x=16, y=64),
# Point(x=47, y=18), Point(x=60, y=56), Point(x=13, y=27), Point(x=61, y=78), Point(x=44, y=36), Point(x=70, y=23),
# Point(x=97, y=79), Point(x=97, y=80), Point(x=83, y=31), Point(x=46, y=23), Point(x=22, y=97), Point(x=14, y=7),
# Point(x=73, y=66), Point(x=25, y=73)]