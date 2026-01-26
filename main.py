def get_biggest(numbers):
    if not numbers:
        return -1
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x: x * 10)    # Мы умножаем СТРОКУ на 10, чтобы получить достаточно длинную строку для сравнения
    return int("".join(numbers))          # Например, для "3" и "30":
                                            # "3" * 10 = "3333333333"
                                            # "30" * 10 = "30303030303030303030"
                                                 # 33 > 30, поэтому 3 будет стоять перед 30

print(get_biggest([1, 2, 3]))
print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))
