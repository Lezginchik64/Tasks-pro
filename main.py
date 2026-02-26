import json


def is_correct_json(string):
    try:
        json.loads(string)  # если преобразование не сработает, вылезает ошибка (except)
        return True
    except json.JSONDecodeError:
        return False


data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
print(is_correct_json(data))

print(is_correct_json('number = 17'))
