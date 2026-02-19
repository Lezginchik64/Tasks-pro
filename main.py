import sys

# 1
print(*[i for i in sys.stdin if not i.lstrip().startswith('#')], sep='')

# 2
[sys.stdout.write(i) for i in sys.stdin if not i.lstrip().startswith('#')]