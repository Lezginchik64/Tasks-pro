str_vov = 'а, у, о, ы, и, э, я, ю, ё, е'.replace(', ', '')
word_index = [ind for ind, lit in enumerate(input()) if lit in str_vov]

for _ in range(int(input())):
    word = input()
    if [ind for ind, lit in enumerate(word) if lit in str_vov] == word_index:
        print(word)
