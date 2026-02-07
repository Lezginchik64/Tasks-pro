from datetime import datetime

# 1
with open('diary.txt', 'r', encoding='utf-8') as f:
    print("\n\n".join(
        sorted(f.read().strip().split('\n\n'), key=lambda x: datetime.strptime(x.split('\n')[0], '%d.%m.%Y; %H:%M'))))

# 2
print('\n\n'.join(sorted(
    open('diary.txt', encoding='utf-8').read().strip().split('\n\n'),
    key=lambda b: datetime.strptime(b.split('\n')[0], '%d.%m.%Y; %H:%M')
)))

# 3
notes = {}
pattern = '%d.%m.%Y; %H:%M'

with open('diary.txt', 'r', encoding='utf-8') as file:
    diary = file.read().split('\n\n')   # Мы режем по пустой строке → получаем отдельные отчёты.
    for note in diary:
        data, text = note.split('\n', 1)    # разделить только ОДИН раз, после первого переноса строки остановиться.
        data = datetime.strptime(data, pattern)
        notes[data] = text

for k, v in sorted(notes.items()):
    print(k)
    print(v)
    print()
