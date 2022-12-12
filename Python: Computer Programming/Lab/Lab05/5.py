n = int(input("Enter the number of lines: "))

for i in range(n):
    if i < int(n/2) + (n%2):
        for j in range(i, -1, -1): #range(เริ่ม i, ถึง 0, ห่างกัน -1)
            print(pow(2, j), end=" ")
    else:
        for k in range(n, i, -1):
            print(pow(2, k-(i+1)), end=" ")
    print()
