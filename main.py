# == Тип данных namedtuple. Часть 2 ==

# == Атрибуты _fields, _field_defaults ==
# Именованные кортежи имеют два дополнительных атрибута: _fields и _field_defaults.
# Первый атрибут содержит кортеж строк, в котором перечислены имена полей.
# Второй атрибут содержит словарь, который сопоставляет имена полей с соответствующими значениями по умолчанию, если таковые имеются.
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])
tim = Person('Тимур', 29, 130)
print(tim)      # Person(name='Тимур', age=29, height=130)
print(tim._fields)      # ('name', 'age', 'height')
print(Person._fields)   # ('name', 'age', 'height')
# Обратите внимание на то, что мы можем обращаться к атрибуту _fields как через переменную (tim), так и через сам тип именованного кортежа (Person).

# С помощью атрибута _fields мы можем создавать новые именованные кортежи на основании уже существующих.
# В следующем примере мы создадим новый именованный кортеж с именем ExtendedPerson, который расширяет старый Person новым полем weight.
Person = namedtuple('Person', ['name', 'age', 'height'])
ExtendedPerson = namedtuple('ExtendedPerson', [*Person._fields, 'weight'])  # распаковка полей старого кортежа
timur = ExtendedPerson('Тимур', 29, 170, 65)
print(timur)        # ExtendedPerson(name='Тимур', age=29, height=170, weight=65)
print(ExtendedPerson._fields)     # ('name', 'age', 'height', 'weight')

# Мы также можем использовать атрибут _fields для перебора полей и их значений с помощью встроенной функции zip():
Person = namedtuple('Person', ['name', 'age', 'height'])
timur = Person('Тимур', 29, 170)
for field, value in zip(Person._fields, timur):
    print(field, '->', value)
# name -> Тимур
# age -> 29
# height -> 170
# Атрибут ._fields вытаскивает кортеж со ВСЕМИ названиями, даже теми, что были переименованы необязательной функцией rename. (типа на '_1', '_2' и т.д.).
# А их мы использовать не сможем при создании нового namedtuple.

# С помощью атрибута _field_defaults мы можем выяснить, какие поля именованного кортежа имеют значения по умолчанию.
# Значения по умолчанию делают поля необязательными.
# Например, предположим, что наш именованный кортеж Person должен включать дополнительное поле для хранения страны, в которой живет человек.
# Поскольку в основном мы работаем с людьми из России, то мы устанавливаем соответствующее значение по умолчанию для поля страны следующим образом:
Person = namedtuple('Person', ['name', 'age', 'height', 'country'], defaults=['Russia'])
                                        # defaults - устанавливает значение по умолчанию для последнего объекта field_names (для country)
timur = Person('Тимур', 29, 170)
print(timur)        # Person(name='Тимур', age=29, height=170, country='Russia')
print(timur._field_defaults)        # {'country': 'Russia'}
print(Person._field_defaults)       # {'country': 'Russia'}
# Если именованный кортеж не предоставляет значений по умолчанию, тогда атрибут _field_defaults содержит пустой словарь.
Person = namedtuple('Person', ['name', 'age', 'height', 'country'])
timur = Person('Тимур', 29, 170, 'Russia')
print(Person._field_defaults)   # {}





# == Методы _make(), _replace(), _asdict() ==
# Напомним, что обычные кортежи (tuple) имеют два встроенных метода:
    # index() — возвращает индекс первого элемента, значение которого равняется переданному значению
    # count() — возвращает количество элементов в кортеже, значения которых равны переданному значению

# Именованные кортежи (тип namedtuple) являются производными от обычных кортежей (тип tuple), поэтому наследуют их методы, а также добавляют три новых: _make(), _replace(), _asdict().
# Имена новых методов (_make(), _replace(), _asdict()) и атрибутов (_fields, _field_defaults) начинаются с подчеркивания, чтобы предотвратить конфликты имен с полями именованных кортежей.

# -- Метод _make() --
# Метод _make() используется для создания именованных кортежей из итерируемых объектов (список, кортеж, строка, словарь и так далее).
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'height'])
timur = Person._make(['Timur', 24, 190])
print(timur)    # Person(name='Timur', age=24, height=190)
# Обратите внимание на то, что метод _make() – это метод типа, а не конкретного экземпляра, поэтому вызывать его нужно через название типа (Person._make).
# Метод _make() работает как альтернативный конструктор типа.


# -- Метод _asdict() --
# Мы можем преобразовывать именованные кортежи в словари с помощью метода _asdict().
# Этот метод возвращает словарь, в котором имена полей используются в качестве ключей.
# Ключи результирующего словаря находятся в том же порядке, что и поля в исходном именованном кортеже.
Person = namedtuple('Person', ['name', 'age', 'height'])
timur = Person._make(['Timur', 12, 150])
print(timur._asdict())  # {'name': 'Timur', 'age': 12, 'height': 150}
# До Python 3.8 метод _asdict() возвращал тип данных OrderedDict.
# В настоящий момент метод возвращает обычный словарь (тип dict), так как сейчас словари запоминают порядок добавления в них ключей.


# -- Метод _replace() --
# Метод _replace() позволяет создавать новые именованные кортежи на основании уже существующих с заменой некоторых значений.
# Потребность в данном методе вызвана тем, что именованные кортежи являются неизменяемыми.
Person = namedtuple('Person', ['name', 'age', 'height', 'country'])
timur1 = Person('Тимур', 29, 170, 'Russia')
timur2 = timur1._replace(age=13, height=190, country='Germany')
print(timur1)   # Person(name='Тимур', age=29, height=170, country='Russia')
print(timur2)   # Person(name='Тимур', age=13, height=190, country='Germany')
# Обратите внимание на то, что метод _replace() не изменяет текущий именованный кортеж, а возвращает новый.