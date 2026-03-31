from collections import Counter

with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    counter = Counter(filter(str.isalpha, file.read().lower()))
    # counter = Counter([line for line in file.read().lower() if line.isalpha()])
for i in sorted(counter):
    print(f'{i}: {counter[i]}')
