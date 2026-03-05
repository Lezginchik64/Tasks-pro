from zipfile import ZipFile
import json


def load_json(s):
    try:
        return json.loads(s)
    except:
        return None


players = []
with ZipFile('data.zip', 'r') as zip_file:
    for file in zip_file.namelist():
        player = load_json(zip_file.read(file))     # читаем файлы из архива - zip_file.read(file) и преобразуем в словарь в функции load_json
        if player and player['team'] == 'Arsenal':
            players.append(f"{player['first_name']} {player['last_name']}")

for i in sorted(players):
    print(i)
# Исходя из теории сначала открывается конкретный файл в ранее открытом зип-файле, чтобы потом можно было считать этот файл
# with zip_file.open(f) as file:
#     d = json.loads(file.read())

# В этой задаче, мы сразу считываем конкретный файл в зипе без создания этого промежуточного файла.
# player = load_json(zip_file.read(file))