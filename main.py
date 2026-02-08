from datetime import datetime, date


def expand(s):
    if '-' in s:
        start_s, end_s = s.split('-')
    else:
        start_s = end_s = s

    start = datetime.strptime(start_s, '%d.%m.%Y').date().toordinal()
    end = datetime.strptime(end_s, '%d.%m.%Y').date().toordinal()
    return set(range(start, end + 1))


def is_available_date(booked_dates, date_for_booking):
    booked_set = set()
    for i in booked_dates:
        booked_set.update(expand(i))

    date_for_booking_set = expand(date_for_booking)

    return date_for_booking_set.isdisjoint(booked_set)


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '12.11.2021'
print(is_available_date(dates, some_date))
