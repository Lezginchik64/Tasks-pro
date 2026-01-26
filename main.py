# 1
def filter_anagrams(word, words):
    return [i for i in words if sorted(word) == sorted(i)]


# 2
def letters(words):
    letters_dict = {}
    for i in words:
        letters_dict[i] = letters_dict.get(i, 0) + 1
    return letters_dict

def filter_anagrams(word, anagrams):
    return [i for i in anagrams if letters(word) == letters(i)]


print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))

word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
print(filter_anagrams(word, anagrams))
