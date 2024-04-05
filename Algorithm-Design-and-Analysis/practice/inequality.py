def solving_inequality(y_val):
    left = 0
    right = 100000000000000000
    result = 0
    while left <= right:
        mid = (right + left) // 2
        equation = (mid * mid) + mid
        if equation == y_val:
            return mid
        elif equation < y_val:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

print(solving_inequality(int(input())))
