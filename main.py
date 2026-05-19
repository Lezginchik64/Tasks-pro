from collections import Counter

words = map(len, input().split())
counts = Counter(words)
for k, v in sorted(counts.items(), key=lambda x: x[1]):
    print(f'Слов длины {k}: {v}')
