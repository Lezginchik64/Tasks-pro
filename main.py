from pathlib import Path

path = Path('/Users/lezginchik/Downloads/Test')

# Возможность конструировать пути с помощью оператора деления /
full_path = path / 'folder1'
print(full_path)    # /Users/lezginchik/Downloads/Test/folder1

# Объекты Path "знают" о себе, являются ли они абсолютными (начинаются от корня файловой системы) или относительными.
print(full_path.is_absolute())  # True

# Разбор пути на компоненты
print(f"Родительская директория: {full_path.parent}")   # Родительская директория: /Users/lezginchik/Downloads/Test
print(f"Имя файла: {full_path.name}")                   # Имя файла: folder1
print(f"Имя без расширения: {full_path.stem}")          # Имя без расширения: folder1
print(f"Расширение: {full_path.suffix}")                # Расширение: (Например: ".jpeg", ".txt" и тд)
print(f"Кортеж из частей пути: {full_path.parts}")      # Кортеж из частей пути: ('/', 'Users', 'lezginchik', 'Downloads', 'Test', 'folder1')

# Атрибут .parents — это особый итератор, который позволяет "подниматься" вверх по дереву каталогов:
print(f"Первый родитель: {full_path.parents[0]}") # Первый родитель: /Users/lezginchik/Downloads/Test
print(f"Второй родитель: {full_path.parents[1]}")  # Второй родитель: /Users/lezginchik/Downloads
    # path.parents[0] это то же самое, что и path.parent

# Проверка существования файла или директории
print(full_path.exists())   # True
print(full_path.is_file())  # False
print(full_path.is_dir())   # True

# Создание директорий
full_path.mkdir(parents=True, exist_ok=True)
    # parents=True — создать родительские директории, если их нет
    # exist_ok=True — не вызывать ошибку, если директория уже существует

# Чтение и запись файлов
content = 'Привет, мир pathlib!'
full_path.write_text(content, encoding='utf-8')          # Запись в файл в одну строку!
read_content = full_path.read_text(encoding='utf-8')     # Чтение из файла в одну строку!
    # Преимущество: Кардинальное сокращение шаблонного кода. Для бинарных файлов существуют аналогичные методы read_bytes() и write_bytes().

# Переименование и перемещение
src = Path('main.log')
dst = Path('main.log.old')
src.rename(dst)     # # Метод rename можно вызвать прямо на объекте

# Удаление файлов и директорий
file_to_del = Path('temp.tmp')
dir_to_del = Path('temp_dir')
file_to_del.unlink()        # .unlink() для файлов (и символических ссылок)
dir_to_del.rmdir()          # .rmdir() для пустых директорий

# Поиск файлов с помощью glob и rglob
    # Вам нужно найти все .src файлы в проекте?
    # .glob(pattern) — ищет файлы по шаблону в текущей директории.
    # .rglob(pattern) — ищет файлы рекурсивно (r от "recursive") во всех поддиректориях.
project_dir = Path('src')
py_files_generator = project_dir.rglob('*.py')      # rglob возвращает генератор, что экономит память
for path_obj in py_files_generator:
    print(f"Найден файл: {path_obj}, размер: {path_obj.stat().st_size} байт")   # Мы сразу получаем Path объекты, готовые к работе!
    # Мы получаем генератор полноценных объектов Path, с которыми можно сразу продолжить работу, например, узнать их размер, как в примере выше.

# Итерация по содержимому директории
    # Получить список всего, что лежит в папке, — базовая задача.
dir_path = Path('src')
for item_path in dir_path.iterdir():    # iterdir() возвращает генератор объектов Path
    if item_path.is_file():     # Мы сразу работаем с полноценными путями
        print(f"Файл: {item_path}")
    # iterdir() избавляет от необходимости вручную склеивать путь к директории с именем файла.
    # Как и glob, он возвращает генератор, что эффективно при работе с очень большими директориями.

# Работа с метаданными файлов
    # Получить размер файла, дату создания или последней модификации теперь можно одним вызовом метода .stat().
print(full_path.stat().st_size)     # размер_файла

# Пример: Поиск 10 самых больших файлов в директории
from pathlib import Path

# Директория для поиска (например, домашняя)
search_dir = Path.home()

# 1. Используем rglob для рекурсивного поиска всех файлов
# 2. Фильтруем, оставляя только файлы (на случай, если попадется ссылка на директорию)
# 3. Создаем список кортежей (размер_файла, путь_к_файлу)
all_files = [
    (p.stat().st_size, p)
    for p in search_dir.rglob('*')
    if p.is_file()
]
# 4. Сортируем список по убыванию размера и берем первые 10
all_files.sort(key=lambda x: x[0], reverse=True)

print("Топ-10 самых больших файлов:")
for size, path in all_files[:10]:
    # Приводим размер к мегабайтам для читаемости
    print(f"  {path.name:<40} | {size / 1024 / 1024:.2f} MB")
