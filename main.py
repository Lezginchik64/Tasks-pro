from collections import Counter

# 1
counts = Counter(input().lower().split())
min_count = min(counts.values())
print(*sorted(filter(lambda x: counts[x] == min_count, counts)), sep=', ')

# 2
words = input().lower().split()
counts = Counter(words)
min_count = min(counts.values())
res = sorted(key for key, value in counts.items() if value == min_count)
print(', '.join(res))