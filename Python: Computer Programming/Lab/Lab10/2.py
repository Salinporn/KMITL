list1 = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]


def remove_the_thirds(lst):
    del lst[3 - 1::3]


remove_the_thirds(list1)
print(list1)
