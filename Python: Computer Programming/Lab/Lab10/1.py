def name_list():
    lst = []

    name = " "
    i = 1
    while name != "":
        name = input(f"Enter name {i}: ")
        if name != "":
            lst += [name]
        else:
            break
        i += 1
    return print(lst)

name_list()
