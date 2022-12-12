sum = 0
for i in range(5):
    n = int(input("Enter an integer: "))
    if abs(sum+n) == abs(sum) + abs(n):
        sum += n
    else:
        sum = n
    print(f"Current sum: {sum}")