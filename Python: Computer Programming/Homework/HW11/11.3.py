def product(*args):
    cartesian = []
    for i in range(len(args)):
        if i == 0:
            for j in args[i]:
                cartesian += [(j,)]
        else:
            cartesian = [n + (m,) for n in cartesian for m in args[i]]
    return cartesian


s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

print(product(s1, s2))
print(product(s1, s2, s3))
print(product(s1))
