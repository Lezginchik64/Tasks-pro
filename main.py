# 1
n = input().split()
num = set(int(i) for i in n if n.count(i) > 1)
print(*sorted(num))

# 2
nums = [int(i) for i in input().split()]
print(*sorted(filter(lambda x: nums.count(x) > 1, set(nums))))
