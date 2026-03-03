from zipfile import ZipFile

# 1
with ZipFile('workbook.zip', 'r') as file:
    files = [i for i in file.infolist() if not i.is_dir()]
    print(len(files))

# 2
with ZipFile('workbook.zip', 'r') as file:
    files = sum(not i.is_dir() for i in file.infolist())
    print(files)