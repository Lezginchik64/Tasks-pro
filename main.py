import pickle


def filter_dump(filename, objects, typename):
    obj = [i for i in objects if type(i) == typename]
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)


filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
