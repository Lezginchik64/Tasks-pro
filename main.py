from zipfile import ZipFile

# 1
with ZipFile('workbook.zip', 'r') as file:
    info = file.infolist()
    min_file = min((i for i in info if i.file_size), key=lambda x: (x.compress_size / x.file_size) * 100)
    print(min_file.filename.split('/')[1])

# 2
with ZipFile('workbook.zip', 'r') as file:
    info = file.infolist()
    k = {ind: (i.compress_size / i.file_size) * 100 for ind, i in enumerate(info) if i.file_size}
    min_k = min(k, key=k.get)
    print(info[min_k].filename.split('/')[1])
