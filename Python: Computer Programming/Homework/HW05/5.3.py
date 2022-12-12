n = int(input("Input: "))

if n > 1:
    while n > 0:
        n = n - 1
        for i in range(0, n):
            for j in range(0, i+1):
                print("*", end=" ")
            print()
        for i in range(n, 0, -1):
            for j in range(0, i+1):
                print("*", end=" ")
            print()
    for k in range(2):
        print("*")
elif n == 1:
    print("*")

else:
    print("Input must be an integer that is greater than or equal to 1")
