n, x, y, a, b = map(int, input().split())
n = [i for i in range(1, n + 1)]
n[x - 1:y] = reversed(n[x - 1:y])
n[a - 1:b] = reversed(n[a - 1:b])
print(*n)
