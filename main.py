from collections import Counter

counter = Counter(input().split(','))
max_len = max(len(word) for word in counter)
for key, val in sorted(counter.items()):
    price = sum(ord(i) for i in key if i.isalpha())
    print(f'{key.ljust(max_len)}: {price} UC x {val} = {price * val} UC')
