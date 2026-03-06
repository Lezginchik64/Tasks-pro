import pickle
import sys

# 1
file_name, *data = map(str.strip, sys.stdin)
with open(file_name, mode='rb') as file:
    f = pickle.load(file)
    print(f(*data))

# 2
with open(input(), mode='rb') as file:
    f = pickle.load(file)
    print(f(*map(str.strip, sys.stdin)))
