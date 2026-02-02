from datetime import date

dates = sorted([date.fromisoformat(input()) for _ in range(int(input()))])
for i in dates:
    print(i.strftime('%d/%m/%Y'))