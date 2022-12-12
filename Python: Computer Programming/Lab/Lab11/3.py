def inverse(dict):
    d = {}
    k = list(dict.keys())
    v = list(dict.values())
    for i in v:
        s = set()
        index = 0
        for j in v:
            if j == i:
                s.add(k[index])
            index += 1
        d[i] = s
    return d


dict = {'a':'1', 'b':'2', 'c':'1', 'd':'3', 'e':'1', 'f':'2'}
print(inverse(dict))