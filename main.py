import calendar

# 1
try:
    s = int(input())
    if s in [i for i in range(1, 13)]:
        print(calendar.month_name[s])   # месяц по введенному числу
    else:
        print("Введено число из недопустимого диапазона")
except ValueError:
    print("Введено некорректное значение")

# 2
import calendar, math
try:
    n = int(input())
    try:
        1/math.sqrt(n)
        print(calendar.month_name[n])
    except:
        print('Введено число из недопустимого диапазона')
except:
    print('Введено некорректное значение')



