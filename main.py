# 1
def same_parity(numbers):
    return [i for i in numbers if numbers[0] % 2 == i % 2]


# 2
def same_parity2(numbers):
    res = list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))
    return res


print(same_parity([6, 0, 67, -7, 10, -20]))
print(same_parity2([6, 0, 67, -7, 10, -20]))
