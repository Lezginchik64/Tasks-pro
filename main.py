from datetime import date


# 1
def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]


# 2
def get_date_range(start, end):
    start = start.toordinal()
    end = end.toordinal()
    if start > end:
        return []
    dates = []
    for i in range(start, end + 1):
        dates.append(date.fromordinal(i))
    return dates


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)
print(*get_date_range(date1, date2), sep='\n')
