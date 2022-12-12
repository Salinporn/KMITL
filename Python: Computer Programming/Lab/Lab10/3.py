def get_the_difference(l1, l2):
    l3 = [x for x in l1 if x not in l2]
    l4 = [x for x in l2 if x not in l1]
    lst = l3 + l4
    return print(lst)


get_the_difference([3,1,1,1,2,7], [4,1,1,2,2,5])