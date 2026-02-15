import timeit, random

l = [random.randrange(1, 100_000) for _ in range(100_000)]


def funk(n):
    return n ** 3


t1 = timeit.timeit('[funk(i) for i in l]', globals=globals(), number=100)   # Код выполнится 100 раз → возвращается общее время этих 100 запусков.
t2 = timeit.repeat('list(map(funk, l))', globals=globals(), number=100, repeat=10)
# Делается 10 независимых замеров, в каждом замере код выполняется по 100 раз, возвращается список из 10 чисел
t3 = timeit.timeit('[i**3 for i in l]', globals=globals(), number=100)

print(f"List funk: {t1}")
print(f"Map: {t2}")
print(f"Map_min: {min(t2)}")
print(f"List: {t3}")
