# 1
def convert(text):
    low_count = len(list(filter(str.islower, text)))
    up_count = len(list(filter(str.isupper, text)))
    if low_count >= up_count:
        return text.lower()
    return text.upper()

# 2
def convert(text):
    low_count = sum(list(map(str.islower, text)))
    up_count = sum(list(map(str.isupper, text)))
    if low_count >= up_count:
        return text.lower()
    return text.upper()


print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))
