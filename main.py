from datetime import date


# 1
def num_of_sundays(year):
    count = 0
    start = date(year, 1, 1).toordinal()
    end = date(year, 12, 31).toordinal()
    for i in range(start, end + 1):
        if date.fromordinal(i).weekday() == 6:
            count += 1
    return count


# 2
def num_of_sundays2(year):
    return date(year, 12, 31).strftime('%U')
# %U - Номер недели в году (неделя начинается с воскресенья). Неделя, предшествующая первому воскресенью, является нулевой.

print(num_of_sundays(2000))
print(num_of_sundays2(2001))
