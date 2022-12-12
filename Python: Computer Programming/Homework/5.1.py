n = float(input("Enter a number n: "))
guess = n/2
x = 4
for i in range(3):
    for j in range(x):
        temp = float(n/guess)
        guess = (guess+temp)/2
    x += 1
    print(f"The result when iterates {x} times = {guess:.3f}")