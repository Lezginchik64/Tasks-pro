from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name, 'r') as zip_file:
        zip_file.extractall(members=args or None)   # если args - пустой, тогда None (members=None - извлечь все файлы)

# С методом extractall() используем необязательный аргумент members. По умолчанию members = None.
# Если members = None, то извлекутся все файлы в архиве.
# Если в members передать список файлов, то извлекутся конкретные файлы.

extract_this('workbook.zip')
