from datetime import datetime as dt

pattern = '%d.%m.%Y'
d = {}
for _ in range(int(input())):
    val, key = input().rsplit(' ', 1)
    d.setdefault(key, []).append(val)

min_date = min(d, key=lambda x: dt.strptime(x, pattern))
names = d[min_date]
print(min_date, (names[0] if len(names) == 1 else len(names)))

# for _ in range(int(input())):
#     val, key = input().rsplit(' ', 1)
#     if key not in d:
#         d[key] = []
#     d[key].append(val)
