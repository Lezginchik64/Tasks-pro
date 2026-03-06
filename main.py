import pickle

# 1
file_name, num = input(), int(input())

with open(file_name, 'rb') as file:
    elem = pickle.load(file)

nums = [i for i in elem if isinstance(i, int)]
check = sum(nums) if isinstance(elem, dict) else max(nums, default=0) * min(nums, default=0)
print(['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][check == num])


# 2
file_name, num = input(), int(input())
with open(file_name, 'rb') as file:
    elem = pickle.load(file)

nums = [i for i in elem if isinstance(i, int)]
if isinstance(elem, list):
    res = min(nums, default=0) * max(nums, default=0)
else:
    res = sum(nums)

print('Контрольные суммы совпадают' if res == num else 'Контрольные суммы не совпадают')
