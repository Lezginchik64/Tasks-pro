from collections import Counter

counts = Counter(input().lower().split())
max_count = max(counts.values())
print(sorted(filter(lambda x: counts[x] == max_count, counts), reverse=True)[0])
