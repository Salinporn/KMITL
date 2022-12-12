isbn = input("Enter the first 9 digits of an ISBN-10 as a string: ")

d = list(map(int, isbn))

d10 = (d[0]+(d[1]*2)+(d[2]*3)+(d[3]*4)+(d[4]*5)+(d[5]*6)+(d[6]*7)+(d[7]*8)+(d[8]*9)) % 11

if d10 != 10:
    print(f"Your ISBN-10 number is {isbn}{d10}")
elif d10 == 10:
    print(f"Your ISBN-10 number is {isbn}X")