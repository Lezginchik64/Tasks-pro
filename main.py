from datetime import datetime, timedelta

# 1
print((datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=int(input()))).time())

# 2
h, m, s = map(int, input().split(':'))
td = timedelta(hours=h, minutes=m, seconds=s) + timedelta(seconds=int(input()))
res = datetime(1, 1, 1) + td
print(res.strftime('%H:%M:%S'))
