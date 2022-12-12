def list_member(n, lst):
    if len(lst) == 0:
        return False
    elif lst[0] == n:
        return True
    else:
        return list_member(n, lst[1:])


print(list_member(2, [1,2,3]))
