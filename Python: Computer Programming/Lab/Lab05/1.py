x = 1
for i in range(5):
    for j in range(i+1):
        print(x, end=" ")
        x += 1
    x = 1
    print()

print("----------")

for k in range(5):
    for l in range(k, 5):
        print(x, end=" ")
        x += 1
    x = 1
    print()
