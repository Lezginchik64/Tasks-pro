from collections import Counter


# 1
def count_occurrences(word, words):
    counter = Counter(words.lower().split())
    return counter[word.lower()]


# 2
def count_occurrences(word, words):
    return Counter(words.lower().split())[word.lower()]


word = 'python'
words = 'Python Conferences python training python events'
print(count_occurrences(word, words))
