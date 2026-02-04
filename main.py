from datetime import date


def is_correct(day, month, year):
    while True:
        try:
            date(year, month, day)
            return True
        except:
            return False


print(is_correct(31, 12, 2021))
print(is_correct(31, 13, 2021))
