from datetime import datetime

# 1
dt = [datetime.strptime(i, '%d.%m.%Y') for i in input().split()]
res = [abs(dt[i] - dt[i - 1]).days for i in range(1, len(dt))]
print(res)

# 2
l = list(map(lambda x: datetime.strptime(x, "%d.%m.%Y"), input().split()))
dif = [abs(v - l[i]).days for i, v in enumerate(l[1:])]
print(dif)