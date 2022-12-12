short = input("Enter a short string: ")
long = input("Enter a long string: ")

tf = False
i = 0
while len(short) + i <= len(long):
    sub = long[i:len(short) + i]
    if short != sub:
        tf = False
    else:
        tf = True
        break
    i += 1
print(tf)
