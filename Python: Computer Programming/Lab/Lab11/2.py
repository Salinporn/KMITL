def find_duplicates(dict):
    dupe = {}
    key = []
    for k, v in dict.items():
        key.append(v)
    key = set([name for name in key if key.count(name) > 1])
    for k, v in dict.items():
        if v in key:
            dupe.update({k: v})
    return dupe


myDict = {'s5301':'Fred', 's5302':'Harry', 's5303':'John', 's5304':'Fred', 's5305':'Harry'}
print(find_duplicates(myDict))
