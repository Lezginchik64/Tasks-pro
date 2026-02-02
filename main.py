from datetime import date

# 1
print(min(date.fromisoformat(input()) for _ in range(2)).strftime('%d-%m (%Y)'))

# 2
date = date.fromisoformat(input())
date1 = date.fromisoformat(input())
print(min(date, date1).strftime('%d-%m (%Y)'))