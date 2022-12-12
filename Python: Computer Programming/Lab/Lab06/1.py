x = input("Enter your marks: ")


def grade(x):
    g = ""
    try:
        x = float(x)
        if 100 >= x >= 0:
            if x >= 80:
                g += "A"
            elif 70 <= x < 80:
                g += "B"
            elif 60 <= x < 70:
                g += "C"
            elif 50 <= x < 60:
                g += "D"
            elif x < 50:
                g += "F"
            print(f"Your grade is {g}")
        else:
            g = g
    except ValueError:
        g = g
    return g


grade(x)
