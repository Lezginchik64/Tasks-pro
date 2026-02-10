from datetime import datetime, date, timedelta


# 1
def fill_up_missing_dates(dates):
    date_list = sorted([datetime.strptime(i, '%d.%m.%Y').toordinal() for i in dates])
    start, end = date_list[0], date_list[-1]
    return [date.fromordinal(i).strftime('%d.%m.%Y') for i in range(start, end + 1)]


# 2
def fill_up_missing_dates(dates):
    pattern = '%d.%m.%Y'
    dates = [datetime.strptime(i, pattern) for i in dates]
    start, end = min(dates), max(dates)
    days = (end - start).days
    return [(start + timedelta(days=i)).strftime(pattern) for i in range(days + 1)]


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))

dates = ['20.07.2021', '16.05.2021', '19.01.2021', '18.11.2021', '17.10.2021', '15.03.2021']
print(len(fill_up_missing_dates(dates)))
