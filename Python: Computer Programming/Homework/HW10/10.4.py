def print_table(lst):
    for row in lst:
        for elem in row:
            print(elem, end="\t")
        print()


print_table([["X", "Y"], [0, 0], [10, 10], [200, 200]])
print_table([["ID", "Name", "Surname"],
             ["001", "Guido", "van Rossum"],
             ["002", "Donald", "Knuth"],
             ["003", "Gordon", "Moore"]])

