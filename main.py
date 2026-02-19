import sys

# 1
d = {}
l = [i for i in sys.stdin]
for line in l[:-1]:
    news, cat, true = line.strip().split(' / ')
    d.setdefault(cat, []).append((news, true))
category = l[-1].strip()
if category in d:
    print(*[i[0] for i in sorted(d[category], key=lambda x: (x[1], x[0]))], sep='\n')

# 2
news = [i.strip().split(' / ') for i in sys.stdin]
true_news = list(filter(lambda x: x[1] == news[-1][0], news[:-1]))
print(*[i[0] for i in sorted(true_news, key=lambda x: (float(x[2]), x[0]))], sep='\n')
