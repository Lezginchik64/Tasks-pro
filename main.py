from datetime import datetime

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
# 1
before = sum(map(lambda x: x.hour < 12, times_of_purchases))
after = sum(map(lambda x: x.hour > 12, times_of_purchases))
print("До полудня" if before > after else 'После полудня')

# 2
print('До полудня' if len(list(filter(lambda x: x.hour < 12, times_of_purchases))) > len(
    times_of_purchases) / 2 else 'После полудня')

# 3
df = [i.strftime('%p') for i in times_of_purchases]  # %p - До полудня или после (при 12-часовом формате) - AM, PM (en_US)
print(["До полудня", "После полудня"][df.count('PM') > df.count('AM')])
# Выражение "dts.count('PM')>dts.count('AM')" является булевым, т.к. здесь проверяется неравенство, поэтому ответ True/False, то есть 1/0.
# В квадратных скобках он используется как индекс к выражению. То же самое что if/else, только в одну строку.
# В первых скобках - список, а во вторых - индекс.
