n = input("Enter an integer: ")

if n == "0":
    print("It is 0")
elif int(n) < 0:
    print("It is negative")
answer = ""
while int(n) > 0:
    bi = int(n) % 2
    n = int(n) / 2
    if bi == 0:
        answer += "0"
    else:
        answer += str(bi)
print(answer[::-1])
