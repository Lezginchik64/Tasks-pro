# 1
letters = [input() for _ in range(3)]
if all(map(lambda x: x in "АаВСсЕеНКМОоРрТХху", letters)):
    print("ru")
elif all(map(lambda x: x in "AaBCcEeHKMOoPpTXxy", letters)):
    print("en")
else:
    print("mix")

# 2
letters = set(input() for _ in range(3))
print('ru' if letters <= set("АаВСсЕеНКМОоРрТХху") else "en" if letters <= set("AaBCcEeHKMOoPpTXxy") else 'mix')
# A <= B - все элементы множества A содержатся в множестве B