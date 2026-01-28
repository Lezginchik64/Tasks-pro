# 1
n = int(input())
langs = set(input().split(', '))
for _ in range(n - 1):      # Мы уже считали первого человека, осталось ещё n-1.
    langs &= set(input().split(', '))       # &= — это оператор пересечения множеств.
                                            # Он оставляет в langs только те элементы, которые есть и в предыдущем множестве, и в новом.
if langs:
    print(*sorted(langs), sep=', ')
else:
    print("Сериал снять не удастся")

# 2
d = {}
n = int(input())
for _ in range(n):
    lang = tuple(input().split(', '))
    for i in lang:
        d[i] = d.get(i, 0) + 1

res = {k for k, v in d.items() if v == n}
if res:
    print(", ".join(sorted(res)))
else:
    print("Сериал снять не удастся")
