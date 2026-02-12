from datetime import datetime as dt

d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(dt.min.toordinal(), dt.max.toordinal() + 1):
    if dt.fromordinal(i).day == 13:
        d[dt.fromordinal(i).weekday()] = d.get(dt.fromordinal(i).weekday(), 0) + 1

print(*d.values(), sep='\n')
