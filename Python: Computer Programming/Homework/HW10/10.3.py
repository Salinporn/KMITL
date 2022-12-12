def my_union(l1, l2):
    for i in l2:
        if i not in l1:
            l1 += [i]
        else:
            continue
    return l1


def my_intersection(l1, l2):
    l3 = []
    for i in range(len(l1)):
        for j in range(len(l1) + 1):
            intersect = l1[i:j]
            if len(intersect) > 0:
                tf = False
                i = 0
                while len(intersect) + i <= len(l2):
                    s = l2[i:len(intersect) + i]
                    if intersect != s:
                        tf = False
                    else:
                        tf = True
                        break
                    i += 1
                if tf:
                    l3 += [intersect]
    intersect = ""
    for k in l3:
        if len(k) > len(intersect):
            intersect = k
    return intersect


def my_difference(l1, l2):
    diff = []
    for i in l1:
        if i not in l2:
            diff += [i]
    return diff


list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

print(my_union(list1, list2))

list4 = my_intersection(list1, list2)
print(list4)

list5 = my_difference(list1, list2)
print(list5)
