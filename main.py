import sys

count, total = 0, 0
for i in sys.stdin:
    try:
        total += float(i)
    except ValueError:
        count += 1

print(int(total) if total.is_integer() else total)
print(count)

# f1 = 2.0
# f2 = 2.2
# print(f1.is_integer(), f2.is_integer())   # True False