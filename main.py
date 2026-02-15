import time as t


def get_the_fastest_func(funcs, arg):
    time = {}
    for func in funcs:
        start = t.monotonic()
        func(arg)
        time[func] = t.monotonic() - start
    return min(time, key=time.get)


def add(a):
    t.sleep(3)
    return a ** 2


def add2(a):
    t.sleep(2)
    return a ** 2


def add3(a):
    t.sleep(1)
    return a ** 2


print(get_the_fastest_func([add, add2, add3], 2))
