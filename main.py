import sys

# 1
print(sum([1 for i in sys.stdin if i.lstrip()[0] == '#']))

# 2
print(sum(1 for row in sys.stdin if row.lstrip().startswith('#')))
