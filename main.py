from zipfile import ZipFile

# 1
with ZipFile('workbook.zip', 'r') as file:
    info = file.infolist()
    size = sum(i.file_size for i in info)
    compress_size = sum(i.compress_size for i in info)
    print(f'Объем исходных файлов: {size} байт(а)')
    print(f'Объем сжатых файлов: {compress_size} байт(а)')

# 2
with ZipFile('workbook.zip') as myzip:
    a, b = map(sum, zip(*[(f.file_size, f.compress_size) for f in myzip.infolist()]))
    print(f'Объем исходных файлов: {a} байт(а)')
    print(f'Объем сжатых файлов: {b} байт(а)')
