# 1
def is_valid(string):
    return all((4 <= len(string) <= 6, string.isdigit()))


# 2
def is_valid(string):
    return string.isdigit() and len(string) in (4, 5, 6)


# 3
def is_valid(string):
    res = [i for i in string if 4 <= len(string) <= 6 and i.isdigit()]
    return len(string) == len(res) and len(string) > 1


print(is_valid('89abc1'))
print(is_valid('4367'))
print(is_valid('900876'))
print(is_valid('49 83'))
print(is_valid(""))
