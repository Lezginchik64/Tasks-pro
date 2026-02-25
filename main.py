# == Работа с json-файлами ==

# -- Формат json --
# JSON (англ. JavaScript Object Notation) — текстовый формат обмена данными, основанный на языке программирования JavaScript.
# Как и многие другие текстовые форматы, JSON легко читается людьми.
# Несмотря на происхождение от JavaScript, формат считается независимым от языка и может использоваться практически с любым языком программирования.



# == Синтаксис json-формата ==
# В отличие от формата csv, данные в формате json не просто разделены запятыми, а чаще всего имеют структуру ключ — значение.
# Это напоминает словарь Python, но в отличие от словаря ключи в json могут быть только строками, заключенными в двойные кавычки.

# Значениями в json-формате могут быть не только строки.
# Это могут быть числа, списки значений, литералы true/false/null, а также вложенные объекты:
# {
#    "firstName": "Тимур",
#    "lastName": "Гуев",
#    "age": 29,
#    "gender": "мужской",
#    "smoke": false,
#    "address": {
#        "streetAddress": "Часовая 25, кв. 127",
#        "city": "Москва",
#        "postalCode": 125315
#    },
#    "phoneNumbers": ["+7 (919) 424-84-34", "+7 (916) 928-92-34"]
# }

# Списки значений, как видно из примера, напоминают списки Python. Они ограничены квадратными скобками, а значения списка указываются через запятую.
# Вложенность данных может быть бесконечной, то есть значением ключа может быть список, а элементом этого списка — объект и так далее.

# Обратите внимание на то, что переносы строк и отступы в формате json необязательны. Они нужны только для удобства чтения.
# Обратите внимание: в формате json используются только двойные кавычки.

# Итак, в качестве значений в json могут быть использованы:
    # число (целое или вещественное)
    # литералы true (истина), false (ложь), null (отсутствие значения)
    # строка (последовательность символов, заключенная в двойные кавычки)
    # список (заключается в квадратные скобки [ ], значения разделяются запятыми). Список может быть пустым, значения в пределах одного списка могут иметь разный тип
    # вложенный объект (неупорядоченное множество пар ключ — значение, заключенное в фигурные скобки { }). Ключ описывается строкой, между ним и значением стоит символ :. Пары ключ — значение отделяются друг от друга запятыми

# Следующий пример показывает json-представление данных об объекте, описывающем человека.
# В данных присутствуют строковые поля имени и фамилии, информация об адресе (вложенный объект) и список телефонов:
# {
#    "firstName": "Тимур",
#    "lastName": "Гуев",
#    "address": {
#        "streetAddress": "Часовая 25, кв. 127",
#        "city": "Москва",
#        "postalCode": 125315
#    },
#    "phoneNumbers": ["+7 (919) 424-84-34", "+7 (916) 928-92-34"]
# }






# == Модуль json ==
# ! Для сериализации данных в json-строку используется функция dumps() из модуля json.
# Для того чтобы сериализовать данные с ее помощью, достаточно передать в нее аргументом любой сериализуемый Python-объект.
# Так как json — текстовый формат, то сериализация в него — это, по сути, преобразование данных в строку.

import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
json_data = json.dumps(data)            # сериализуем словарь data в json-строку

print(type(json_data))   # <class 'str'>
print(json_data)        # {"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}
print()



# == Функция dump() ==
# ! В отличие от функции dumps(), которая преобразует (сериализует) Python-объект в json-строку,
# функция dump() записывает переданный Python-объект в файл.
import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
with open('file.json', 'w') as file:
    json.dump(data, file)
# создает файл file.json и сохраняет в него информацию из словаря data в json-формате.
# Если открыть файл countries.json, мы увидим, что json выведен в одну строку без форматирования:
# {"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}



# -- Необязательные аргументы indent, sort_keys и separators --
# Функции dumps() и dump() имеют необязательные аргументы indent, sort_keys и separators, которые можно использовать для более удобного чтения человеком.

# ! Аргумент indent задает отступ от левого края и по умолчанию имеет значение None для более компактного представления без отступов.
import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
json_data1 = json.dumps(data, indent=2)
json_data2 = json.dumps(data, indent=10)
print(json_data1)
print(json_data2)
# {
#   "name": "Russia",
#   "phone_code": 7,
#   "capital": "Moscow",
#   "currency": "RUB"
# }
# {
#           "name": "Russia",
#           "phone_code": 7,
#           "capital": "Moscow",
#           "currency": "RUB"
# }

# Если значением indent является строка, то она используется в качестве отступа.
json_data = json.dumps(data, indent='++++')
# {
# ++++"name": "Russia",
# ++++"phone_code": 7,
# ++++"capital": "Moscow",
# ++++"currency": "RUB"
# }



# ! Аргумент sort_keys задает сортировку ключей в результирующем json. По умолчанию имеет значение False для более быстрого создания json.
# Если установить значение аргумента True, то ключи будут отсортированы в алфавитном порядке, что особенно удобно, когда ключей много.
import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

json_data1 = json.dumps(data, indent=3)
json_data2 = json.dumps(data, indent=3, sort_keys=True)
print(json_data1)
print(json_data2)
# {
#    "name": "Russia",
#    "phone_code": 7,
#    "capital": "Moscow",
#    "currency": "RUB"
# }
# {
#    "capital": "Moscow",
#    "currency": "RUB",
#    "name": "Russia",
#    "phone_code": 7
# }



# ! Аргумент separators задает кортеж, состоящий из двух элементов (item_separator, key_separator), которые представляют разделители для элементов и ключей.
# По умолчанию аргумент имеет значение (', ', ': ').
import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
json_data = json.dumps(data, indent=3, separators=(';', ' = '))
print(json_data)
# {
#    "name" = "Russia";
#    "phone_code" = 7;
#    "capital" = "Moscow";
#    "currency" = "RUB"
# }





# == Функция loads() ==
# ! Для десериализации данных нужно использовать функцию loads(). Ее аргумент — это строка с данными в формате json.
import json

json_data = '{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}'
data = json.loads(json_data)
print(type(data))   # <class 'dict'>
print(data)     # {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

# Как видно из примера, функция loads() десериализует json-строку в словарь.
# Если строка для десериализации содержит данные с ошибкой, то модуль json не сможет правильно прочитать такую строку, и программа завершится с ошибкой.



# == Функция load() ==
# ! В отличие от функции loads(), которая в качестве аргумента принимает строку с данными в формате json, функция load()
# принимает файловый объект и возвращает его десериализованное содержимое.

# Пусть файл data.json имеет следующее содержимое:
# {
#   "name": "Russia",
#   "phone_code": 7,
#   "capital": "Moscow",
#   "cities": ["Abakan", "Almetyevsk", "Anadyr", "Anapa", "Arkhangelsk", "Astrakhan"],
#   "currency": "RUB"
# }

with open('data.json') as file:
    data = json.load(file)          # # передаем файловый объект
    for key, val in data.items():
        print(f'{key}: {", ".join(val)}')
    else:
        print(f'{key}: {val}')
# читает содержимое файла data.json в словарь data и выводит его содержимое:
# name: Russia
# phone_code: 7
# capital: Moscow
# cities: Abakan, Almetyevsk, Anadyr, Anapa, Arkhangelsk, Astrakhan
# currency: RUB





# == Типы данных в json ==

import json

json_data = '''
{
   "name": "Russia",
   "phone_code": 7,
   "latitude": 60.0,
   "capital": "Moscow",
   "timezones": ["Anadyr", "Barnaul", "Moscow", "Kirov"],
   "translations": {
      "nl": "Rusland",
      "hr": "Rusija",
      "de": "Russland",
      "es": "Rusia",
      "fr": "Russie",
      "it": "Russia"
   }
}'''

data = json.loads(json_data)

print(type(data['name']))       # <class 'str'>
print(type(data['phone_code'])) # <class 'int'>
print(type(data['latitude']))   # <class 'float'>
print(type(data['timezones']))  # <class 'list'>
print(type(data['translations']))   # <class 'dict'>

# Таким образом, модуль json автоматически определяет тип значения при десериализации.
# Такая автоматическая работа с типами данных выгодно отличает json от csv, при работе с которым таких автоматических преобразований нет.



# -- Изменение типа данных --
# Еще один важный аспект преобразования данных в формат json: данные не всегда будут того же типа, что исходные данные в Python.
# Например, кортежи при записи в json превращаются в списки.
import json

data = {
        'name': 'Russia',
        'phone_code': 7,
        'latitude': 60.0,
        'capital': 'Moscow',
        'timezones': ('Anadyr', 'Barnaul', 'Moscow', 'Kirov')
       }

json_data = json.dumps(data)        # преобразуем dict в json
new_data = json.loads(json_data)    # преобразуем json в dict
print(data == new_data) # False
# Так происходит из-за того, что в json используются другие типы данных, и не для всех типов данных Python есть соответствия.

# Таблица конвертации типов данных Python в json:
    # Python	    json
    # dict	        object
    # list, tuple	array
    # str	        string
    # int, float	number
    # True	        true
    # False	        false
    # None	        null

# Таблица конвертации json в типы данных Python:
    # json	            Python
    # object	        dict
    # array	            list
    # string	        str
    # number (int)	    int
    # number (real)	    float
    # true	            True
    # false	            False
    # null          	None



# -- Ограничение по типам данных --
# В формат json нельзя записать словарь, у которого ключи – кортежи.
import json

data = {
        'beegeek': 2018,
        ('Timur', 'Guev'): 29,
        ('Arthur', 'Kharisov'): 20,
        'stepik': 2013
       }

json_data = json.dumps(data)        # преобразуем dict в json
print(json_data)
# Ошибка: TypeError: keys must be str, int, float, bool or None, not tuple

# С помощью необязательного аргумента skipkeys можно игнорировать подобные ключи.
import json

data = {
        'beegeek': 2018,
        ('Timur', 'Guev'): 29,
        ('Arthur', 'Kharisov'): 20,
        'stepik': 2013
       }

json_data = json.dumps(data, skipkeys=True)        # преобразуем dict в json
print(json_data)     # {"beegeek": 2018, "stepik": 2013}

# Кроме того, в json ключами словаря могут быть только строки.
# Но если в словаре Python использовались числа, булевы значения или None, то ошибки не будет, вместо этого они будут преобразованы в строки.
import json

data = {1: 'Timur', False: 'Arthur', None: 'Ruslan'}
json_data = json.dumps(data)
print(json_data)    # {"1": "Timur", "false": "Arthur", "null": "Ruslan"}





# == Кириллические символы в json ==
import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
s = json.dumps(data)
print(s)    # {"firstName": "\u0422\u0438\u043c\u0443\u0440", "lastName": "\u0413\u0443\u0435\u0432"}
# Результат, скорее всего, будет неожиданным. Каждая буква из строк Тимур и Гуев будет заменена на ее код.
# Эти коды стандартны, и код для каждой из букв индивидуален. Например. 0438 — код буквы и.

# Обратное преобразование из строки в словарь вернет закодированное значение в первоначальный вид.
import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
s = json.dumps(data)
print(s)        # {"firstName": "\u0422\u0438\u043c\u0443\u0440", "lastName": "\u0413\u0443\u0435\u0432"}
result = json.loads(s)
print(result)   # {'firstName': 'Тимур', 'lastName': 'Гуев'}

# Благодаря стандартным кодам символы будут прочитаны и преобразованы в нужный вид любой программой на любом языке программирования.

# ! С помощью необязательного аргумента ensure_ascii функций dumps() и dump() можно отказаться от такого кодирования.
import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
s = json.dumps(data, ensure_ascii=False)
print(s)        # {"firstName": "Тимур", "lastName": "Гуев"}
result = json.loads(s)
print(result)       # {'firstName': 'Тимур', 'lastName': 'Гуев'}
# Python преобразует такую строку обратно в словарь без проблем (поскольку использует Unicode по умолчанию),
# но нужно помнить, что это может привести к проблемам с преобразованием в программах, написанных на других языках программирования.




# == Примечания ==
# Примечание 4. json – это текстовый формат, что означает, что мы должны открыть файл в текстовом режиме и указать кодировку.
# Вы никогда не ошибетесь, используя UTF-8.

# Примечание 5. Мы можем сериализовать любой объект, поддерживаемый форматом json, например, число, список, строку и так далее.
import json

colors = ['white', 'red', 'black']

with open('list.json', 'w') as file:
    json.dump(colors, file, indent='---')
# создает файл list.json со следующим содержанием:
# [
# ---"white",
# ---"red",
# ---"black"
# ]

# Примечание 6. В формате json ключом может быть только строка.
# Как правило, регистр учитывается программами — имена с буквами в разных регистрах считаются разными.
# Повторяющиеся имена ключей допустимы, но не рекомендуются стандартом;
# обработка таких ситуаций происходит на усмотрение программного обеспечения, возможные варианты: учитывать только первый такой ключ, учитывать только последний такой ключ, генерировать ошибку.
import json

data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'firstName': 'Теймур', 'FirstName': 'Тим'}
s = json.dumps(data, ensure_ascii=False)
print(s)    # {"firstName": "Теймур", "lastName": "Гуев", "FirstName": "Тим"}


# Примечание 11. Мы производили преобразования между объектами языка Python и json-объектами.
# Такие преобразования называются сериализацией (кодирование в json-формат, то есть в поток байтов) и десериализацией (декодирование в объект языка).