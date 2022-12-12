i = int(input("Enter a number: "))

number = ["one", "two", "three", "four", "five", "six",
          "seven", "eight", "nine"]
teen = ["eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
tenth = ["ten", "twenty", "thirty", "forty", "fifty",
         "sixty", "seventy", "eighty", "ninety"]
eng = ""
if i <= 999 and i >= 0:
    if i == 0:
        eng += "zero"
    elif (i//100) >= 1:
        eng += number[(i//100)-1] + " hundred "
        i = i % 100
        if (i // 10) > 1:
            eng += "and " + tenth[(i // 10) - 1]
            i = i % 10
            if (i % 10) > 0:
                eng += "-" + number[(i % 10) - 1]
        elif (i // 10) == 1 and (i % 10) != 0:
            eng += "and " + teen[(i % 10) - 1]
        else:
            if (i % 10) > 0:
                eng += "and " + number[(i % 10) - 1]
            else:
                eng += "and ten"
    else:
        if (i//10) > 1:
            eng += tenth[(i // 10) - 1]
            i = i % 10
            if (i % 10) > 0:
                eng += "-" + number[(i % 10) - 1]
        elif (i // 10) == 1 and (i % 10) != 0:
            eng += teen[(i % 10) - 1]
        else:
            if (i % 10) > 0:
                eng += number[(i % 10) - 1]
            else:
                eng += "ten"
    print(eng)
else:
    print("I don't know.")
