from zipfile import ZipFile
import datetime as dt


with ZipFile('workbook.zip', 'r') as file:
    info = file.infolist()
    for i in sorted(info, key=lambda x: x.filename.split('/')[-1]):
        if not i.is_dir():
            print(i.filename.split('/')[-1])
            print(f'  Дата модификации файла: {dt.datetime(*i.date_time)}')
            print(f'  Объем исходного файла: {i.file_size} байт(а)')
            print(f'  Объем сжатого файла: {i.compress_size} байт(а)')
            print()