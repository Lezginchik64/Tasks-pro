from datetime import date

early_hurricanes = 0
hurricane_andrew = [date(2021, 12, 31), date(2025, 3, 19), date(2017, 5, 25)]
for hurricane in hurricane_andrew:
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)
