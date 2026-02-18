import sys

# 1
numbers = [int(line.strip("\n")) for line in sys.stdin]
print("Анри" if (len(numbers) + numbers[-1]) % 2 else "Дима")

# 2
s = tuple(int(i.strip()) for i in sys.stdin.readlines())
print(('Дима', 'Анри')[(len(s) - 1) % 2 == s[-1] % 2])
