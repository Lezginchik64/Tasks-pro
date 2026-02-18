import sys

# 1
d = list(map(lambda x: x[::-1].strip(), sys.stdin))
print(*d, sep='\n')

# 2
for line in sys.stdin:
    print(line.strip()[::-1])
