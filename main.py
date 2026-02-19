import sys

l = [int(i.strip()) for i in sys.stdin]
if l:
    print(f'Рост самого низкого ученика: {min(l)}')
    print(f'Рост самого высокого ученика: {max(l)}')
    print(f'Средний рост: {sum(l) // len(l)}')
else:
    print('нет учеников')