from collections import Counter

inp = input().lower().split()
print(Counter(inp).most_common()[0][0])