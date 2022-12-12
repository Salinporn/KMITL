def composite(dict1, dict2):
    d = {}
    for key1 in dict1:
        for key2 in dict2:
            value1 = dict1[key1]
            value2 = dict2[key2]
            if key2 == value1:
                d[key1] = value2
    return d


dict1 = {'a': 'p', 'b': 'r', 'c': 'q', 'd': 'p', 'e': 's'}
dict2 = {'p': '1', 'q': '2', 'r': '3'}

print(composite(dict1, dict2))
