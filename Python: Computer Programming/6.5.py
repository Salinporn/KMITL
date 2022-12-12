m = int(input("Input your amount of money: "))

money = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
for i in money:
    number = m // i
    m = m % i
    if number != 0:
        if i > 10:
            print(f"{i}-Baht notes: {number}")
        else:
            print(f"{i}-Baht coins: {number}")
    else:
        continue
