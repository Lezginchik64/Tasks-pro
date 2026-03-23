from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)]

# 1
res = defaultdict(int)
for key, val in data:
    res[key] += val
for k, v in sorted(res.items()):
    print(f'{k}: ${v}')

# 2
res = defaultdict(list)
for i in data:
    res[i[0]].append(i[1])
for k, v in sorted(res.items()):
    print(f'{k}: ${sum(v)}')
