def index_of_nearest(numbers, number):
    return numbers.index(min(numbers, key=lambda x: abs(number - x))) if numbers else -1


print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
