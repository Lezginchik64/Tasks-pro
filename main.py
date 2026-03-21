from collections import namedtuple

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

dictforsort = {'Gold': 0, 'Silver': 1, 'Bronze': 2, 'Basic': 3}
sort_users = sorted(users, key=lambda x: (dictforsort[x.plan], x.email))
# sort_users = sorted(users, key=lambda x: (('Gold', 'Silver', 'Bronze', 'Basic').index(x.plan), x.email))
for user in sort_users:
    print(f'{user.name} {user.surname}')
    print(f'  Email: {user.email}')
    print(f'  Plan: {user.plan}\n')

# sort_users = sorted(users, key=lambda x: (('Gold', 'Silver', 'Bronze', 'Basic').index(x.plan), x.email))
# Разбор сортировки:
# index(x.plan) - это индекс элемента из кортежа ('Gold', 'Silver', 'Bronze', 'Basic'). Проще на примере.
# Допустим, у нас x.plan у данного User'a ,будет 'Gold'. Тогда получаем  ('Gold', 'Silver', 'Bronze', 'Basic').index('Gold').
# А какой индекс у элемента 'Gold' в этом кортеже? Ноль. Соответственно,  приоритет у него выше и он выведется раньше.
