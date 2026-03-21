from collections import namedtuple
import pickle

# 1
Animal = namedtuple('Animal', ('name', 'family', 'sex', 'color'))
with open('data.pkl', 'rb') as file:
    reader = pickle.load(file)
    for i in reader:
        print(f'name: {i.name}')
        print(f'family: {i.family}')
        print(f'sex: {i.sex}')
        print(f'color: {i.color}\n')

# 2
with open('data.pkl', 'rb') as f:
    for animal in pickle.load(f):
        print('name: {}\nfamily: {}\nsex: {}\ncolor: {}\n'.format(*animal))
# name: Alex
# family: dogs
# sex: m
# color: brown
#
# name: Nancy
# family: cats
# sex: w
# color: white