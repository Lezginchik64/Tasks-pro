from datetime import date


def print_good_dates(dates):
    if dates:
        sort_dates = sorted(filter(lambda x: x.year == 1992 and x.day + x.month == 29, dates))
        print(*map(lambda i: i.strftime("%B %d, %Y"), sort_dates), sep='\n')


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)

print_good_dates([])
