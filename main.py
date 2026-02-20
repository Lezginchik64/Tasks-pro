import sys

# 1
num = [int(i) for i in sys.stdin]
a = map(lambda a, b: b - a, num, num[1:])
b = map(lambda a, b: b // a, num, num[1:])
if len(set(a)) == 1:
    print("Арифметическая прогрессия")
elif len(set(b)) == 1:
    print("Геометрическая прогрессия")
else:
    print("Не прогрессия")

# 2
num = [int(i.strip()) for i in sys.stdin]
arif = set([num[i] - num[i - 1] for i in range(1, len(num))])
geom = set([num[i] // num[i - 1] for i in range(1, len(num))])
if len(arif) == 1:
    print("Арифметическая прогрессия")
elif len(geom) == 1:
    print("Геометрическая прогрессия")
else:
    print("Не прогрессия")