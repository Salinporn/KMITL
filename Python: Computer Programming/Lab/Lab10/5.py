l1 = input("Enter list1: ")
l2 = input("Enter list2: ")


def merge(l1, l2):
    l3 = l1 + l2
    for i in range(len(l3)):
        for j in range(i + 1, len(l3)):
            if l3[i] > l3[j]:
                l3[i], l3[j] = l3[j], l3[i]
    return l3

# l1 = [1, 5, 16, 61, 111]
# l2 = [2, 4, 5, 6]


print(merge(l1, l2))
