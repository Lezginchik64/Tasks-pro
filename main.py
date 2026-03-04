from zipfile import ZipFile
import datetime as dt

# 1
with ZipFile('workbook.zip', 'r') as file:
    info = file.infolist()
    d = (2021, 11, 30, 14, 22)
    dates = [i.filename.split('/')[-1] for i in info if i.date_time > d and not i.is_dir()]
    print(*sorted(dates), sep='\n')

# 2
dates = [info[i].filename.split('/')[-1] for i in range(len(info)) if
         dt.datetime(*info[i].date_time) > dt.datetime(*d) and not info[i].is_dir()]
