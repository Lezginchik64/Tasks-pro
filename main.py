groups = {}
for i in range(1, int(input()) + 1):
    nums_sum = sum(map(lambda x: int(x), str(i)))
    groups[nums_sum] = groups.get(nums_sum, 0) + 1
print(max(groups.values()))
# ключ словаря groups - это сумма цифр
# значение - сколько чисел имеет такую сумму цифр