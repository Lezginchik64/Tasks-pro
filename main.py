# == Модуль calendar ==
# По умолчанию модуль calendar следует григорианскому календарю, где понедельник является первым днем недели (имеет номер 0), а воскресенье — последним днем недели (имеет номер 6).
# В отличие от уже изученных модулей datetime и time, которые также предоставляют функции, связанные с календарем, модуль calendar предоставляет основные функции, связанные с отображением и манипулированием календарями.



# == Атрибуты модуля calendar ==
# В отличие от функций, выполняющих определенную работу, в модуле calendar есть атрибуты, которые возвращают константные (общепринятые) значения, полезные при решении практических задач.


# -- Атрибут day_name --
# Атрибут calendar.day_name возвращает итерируемый объект, содержащий названия дней недели на английском языке.
import calendar

for name in calendar.day_name:
    print(name)
print()
# Monday
# Tuesday
# Wednesday
# Thursday
# Friday
# Saturday
# Sunday
# Обратите внимание на то, что при обращении к атрибуту мы не ставим скобки, которые ставим при вызове функции.

# Для локализации на русский язык мы используем код:
import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
for name in calendar.day_name:
    print(name)
print()
# понедельник
# вторник
# среда
# четверг
# пятница
# суббота
# воскресенье

# Для преобразования итерируемого объекта в список мы используем следующий код:
import calendar

names = list(calendar.day_name)
print(names)
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']




# -- Атрибут day_abbr --
# Атрибут calendar.day_abbr возвращает итерируемый объект, содержащий сокращенные названия дней недели.
import calendar, locale

for name in calendar.day_abbr:
    print(name)

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

for name in calendar.day_abbr:
    print(name)
# Mon
# Tue
# Wed
# Thu
# Fri
# Sat
# Sun
# Пн
# Вт
# Ср
# Чт
# Пт
# Сб
# Вс




# -- Атрибут month_name --
# Атрибут calendar.month_name возвращает итерируемый объект, содержащий названия месяцев года.
import calendar, locale

english_names = list(calendar.month_name)
print(english_names)
# ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

russian_names = list(calendar.month_name)
print(russian_names)
# ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

# Обратите внимание: атрибут month_name соответствует обычному соглашению, что январь – это месяц номер 1, поэтому список имеет длину в 13 элементов, первый из которых – пустая строка.




# -- Атрибут month_abbr --
# Атрибут calendar.month_abbr возвращает итерируемый объект, содержащий сокращенные названия месяцев года.
import calendar, locale

english_names = list(calendar.month_abbr)
print(english_names)
# ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

russian_names = list(calendar.month_abbr)
print(russian_names)
# ['', 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']




# -- Атрибуты номеров дней недели --
# Для получения номеров дней недели можно использовать атрибуты MONDAY, TUESDAY, ..., SUNDAY.
import calendar

print(calendar.MONDAY)      # 0
print(calendar.TUESDAY)     # 1
print(calendar.WEDNESDAY)   # 2
print(calendar.THURSDAY)    # 3
print(calendar.FRIDAY)      # 4
print(calendar.SATURDAY)    # 5
print(calendar.SUNDAY)      # 6
print()





# == Функции модуля calendar ==
# Модуль calendar содержит множество полезных функций. Приведем основные из них.


# -- Функция setfirstweekday() --
# По умолчанию в модуле calendar понедельник является первым днем недели (имеет номер 0), а воскресенье – последним днем недели (имеет номер 6).
# Функция setfirstweekday() позволяет изменить поведение по умолчанию и устанавливает заданный день недели в качестве начала недели.
# Например, чтобы установить в качестве первого дня воскресенье, мы используем следующий код:
import calendar

calendar.setfirstweekday(calendar.SUNDAY)     # эквивалентно calendar.setfirstweekday(6)
# На практике следует использовать константы calendar.MONDAY, calendar.TUESDAY, ...,calendar.SUNDAY , а не значения 0, 1, ..., 6.



# -- Функция firstweekday() --
# Функция firstweekday() возвращает целое число, означающее день недели, установленный в качестве начала недели.
print(calendar.firstweekday())      # 0
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.firstweekday())      # 6



# -- Функция isleap() --
# В курсе «Поколение Python: курс для начинающих» мы решали задачу, в которой требовалось проверить, является ли год високосным.
# Напомним, что год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
# Модуль calendar содержит функцию isleap(), которая осуществляет нужную проверку.
import calendar

print(calendar.isleap(2020))    # True
print(calendar.isleap(2021))    # False



# -- Функция leapdays() --
# Функция leapdays(y1, y2) возвращает количество високосных лет в диапазоне от y1 до y2 (не включительно), где y1 и y2 – годы.
import calendar

print(calendar.leapdays(2020, 2025))    # 2
# так как в нужном диапазоне [2020;2025) находятся два високосных года: 2020 и 2024.
# Эта функция работает для диапазонов, охватывающих смену столетий.



# -- Функция weekday() --
# Функция weekday(year, month, day) возвращает день недели в виде целого числа (где 0 – понедельник, 6 – воскресенье) для заданной даты.
# Аргументы функции:
    # year – год начиная с 1970
    # month – месяц в диапазоне 1−12
    # day – число в диапазоне 1−31
import calendar

print(calendar.weekday(2021, 9, 1))     # среда
print(calendar.weekday(2021, 9, 2))     # четверг
# 2
# 3



# -- Функция monthrange() --
# Функция monthrange(year, month) возвращает день недели первого дня месяца и количество дней в месяце в виде кортежа для указанного года year и месяца month.
import calendar

print(calendar.monthrange(2022, 1))     # январь 2022 года
print(calendar.monthrange(2021, 9))     # сентябрь 2021 года
# (5, 31)
# (2, 30)



# -- Функция monthcalendar() --
# Функция monthcalendar(year, month) возвращает матрицу, представляющую календарь на месяц. Каждая строка матрицы представляет неделю.
import calendar

print(*calendar.monthcalendar(2021, 9), sep='\n')
# [0, 0, 1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10, 11, 12]
# [13, 14, 15, 16, 17, 18, 19]
# [20, 21, 22, 23, 24, 25, 26]
# [27, 28, 29, 30, 0, 0, 0]
# Обратите внимание на то, что дни, которые не входят в указанный месяц, представлены нулями.
# При этом каждая неделя начинается с понедельника, если иное не установлено функцией setfirstweekday().



# -- Функция month() --
# Функция month(year, month, w=0, l=0) возвращает календарь на месяц в многострочной строке.
# Аргументами функции являются: year (год), month (месяц), w (ширина столбца даты) и l (количество строк, отводимое на неделю).
# Аргументы w и l имеют значения по умолчанию, поэтому их можно не передавать явно при вызове функции.

print(calendar.month(2026, 6))
#  июня 2026
# вс пн вт ср чт пт сб
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30



# -- Функция calendar() --
# Функция calendar(year, w=2, l=1, c=6, m=3) возвращает календарь на весь год в виде многострочной строки. Аргументами функции являются:
# year (год), w (ширина столбца даты), l (количество строк, отводимые на неделю), c (количество пробелов между столбцами месяцев), m (количество столбцов).
# Аргументы w, l, c, m имеют значения по умолчанию, поэтому их можно не передавать явно при вызове функции.
import calendar

print(calendar.calendar(2026))
# в выводе полный календарь на год

import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
print(calendar.calendar(2026, m=4))
# календарь на русском



# -- Функции prmonth(), prcal() --
# Функция prmonth(theyear, themonth, w=0, l=0) печатает календарь на месяц, возвращенный функцией month(theyear, themonth, w=0, l=0).
# Функция prcal(year, w=0, l=0, c=6, m=3) печатает календарь на весь год, возвращенный функцией calendar(year, w=0, l=0, c=6, m=3).
import calendar

calendar.prmonth(2021, 9)   # календарь на месяц
calendar.prcal(2021)                        # календарь на год

# эквивалентен коду:
import calendar

print(calendar.month(2021, 9))
print(calendar.calendar(2021))




# == Примечания ==
# Примечание. Объекты, доступные по атрибутам day_name, day_abbr, month_name и month_abbr, поддерживают индексацию.
import calendar

print(calendar.day_name[1])
print(calendar.day_abbr[1])
print(calendar.month_name[1])
print(calendar.month_abbr[1])
# Tuesday
# Tue
# January
# Jan