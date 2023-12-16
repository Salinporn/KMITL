
def binary_search(num, numList):
    if len(numList) == 0:
        return False
    else:
        mid = len(numList) // 2
        if numList[mid] == num:
            return mid
        else:
            if numList[mid] < num:
                result = binary_search(num, numList[mid + 1:])
                return result + mid + 1 if result is not False else False
            else:
                return binary_search(num, numList[:mid])

print(binary_search(0, [2, 3, 4, 7, 8]))