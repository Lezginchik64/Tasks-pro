from collections import defaultdict

def wins(pairs):
    res = defaultdict(set)
    for win, lose in pairs:
        res[win].add(lose)
    return res

result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))