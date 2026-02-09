from datetime import date

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)
days = (birthday - today).days
print(days)
