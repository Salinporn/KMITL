def list_reverse(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst.pop()] + list_reverse(lst)


print(list_reverse([1, 2, 3]))