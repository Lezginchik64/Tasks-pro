from collections import defaultdict


def flip_dict(dict_of_lists):
    res = defaultdict(list)
    for key, val in dict_of_lists.items():
        for elem in val:
            res[elem].append(key)
    return res


print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))
