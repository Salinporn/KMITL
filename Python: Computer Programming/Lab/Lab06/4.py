x = input("Integer: ")


def sum_of_digits(x):
    sum_of_digits = 0
    for digit in x:
        sum_of_digits += int(digit)
    print(sum_of_digits)
    return sum_of_digits


sum_of_digits(x)
