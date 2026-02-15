import time as t


def calculate_it(funk, *args):
    start = t.monotonic()
    return funk(*args), t.monotonic() - start


def add(a, b, c):
    t.sleep(3)
    return a + b + c


print(calculate_it(add, 1, 2, 3))
