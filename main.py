from datetime import datetime, timedelta

# 1
h, m, s = map(int, input().split(':'))
td = timedelta(hours=h, minutes=m, seconds=s)
print(td.seconds)

# 2
pattern = '%H:%M:%S'
start = datetime.strptime('00:00:00', pattern)
data = datetime.strptime(input(), pattern)
print(int((data - start).total_seconds()))
