from pathlib import Path

path = Path('/Users/lezginchik/Downloads/Test')

# Поиск файлов
glb = path.glob('*.png')  # поиск png файлов
for f in glb:
    print(f.name)

#  Поиск файлов 2 способ
for file in path.iterdir():  # поиск png файлов
    if file.is_dir():
        continue
    if file.suffix == '.png':
        print(file.name)

# Создание и чтение файла
new_path = path / 'info.txt'
text = 'Pathlib is awesome!'
new_path.write_text(text, encoding='utf-8')  # создание файла с текстом
reader = new_path.read_text(encoding='utf-8')  # чтение файла
print(reader)

# Создание дерева директорий
path2 = path / "data" / "raw" / "logs"
path2.mkdir(parents=True, exist_ok=True)

# Пакетное переименование
for file in path.glob('report-*'):
    new_file = file.with_name(file.name + '.old')
    file.rename(new_file)
