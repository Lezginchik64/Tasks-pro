import json
import sys

data = json.load(sys.stdin)
for k, v in data.items():
    if isinstance(v, list):     # Функция isinstance() - для проверки соответствия типа объекта какому-либо типу данных.
        v = ', '.join(map(str, v))
    print(f'{k}: {v}')
