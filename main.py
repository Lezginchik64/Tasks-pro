from zipfile import ZipFile
import os.path

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

# 1
with ZipFile('files.zip', 'w') as file:
    [file.write(i) for i in file_names if os.path.getsize(i) <= 100]
# Получить объем файла в байтах позволяет функция getsize() из модуля os.path.
# Данная функция принимает в качестве аргумента путь к файлу и возвращает размер указанного файла в байтах.


# 2
with ZipFile('files.zip', 'w') as zip_file:
    for f in file_names:
        with open(f, 'rb') as bite_file:  # rb - открывает файл в режиме «только для чтения» в двоичном формате (исп для pdf, mp3, png и тд)
            data = bite_file.read(101)  # считываем только до 101 байта, если больше, то не считывается (эффективнее на больших файлах)
            size = len(data)
            if size <= 100:
                zip_file.write(f)