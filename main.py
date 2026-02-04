from datetime import date


# 1
def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


count = 0
date1 = input()
while date1 != 'end':
    if is_correct(*map(int, date1.split('.'))):
        count += 1
        print("Корректная")
    else:
        print("Некорректная")
    date1 = input()
print(count)


# 2
# Этот вариант отличается от 1 тем, что тут я изменял работу самой функции is_correct()
def is_correct(dates):
    while True:
        try:
            day, month, year = dates.split(".")
            date(int(year), int(month), int(day))
            return True
        except:
            return False


correct = 0
data1 = input()
while data1 != "end":
    if is_correct(data1):
        correct += 1
        print("Корректная")
    else:
        print("Некорректная")
    data1 = input()
print(correct)
