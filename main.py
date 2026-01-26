# 1
def spell(*args):
    return {k[0].lower(): len(k) for k in sorted(args, key=len)}


# 2
def spell(*args):
    res = {}
    for word in args:
        key = word[0].lower()
        if key not in res or len(word) > res[key]:
            res[key] = len(word)
    return res


words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))

print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))

words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
