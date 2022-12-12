name = input("Enter your name: ")
age = float(input("Enter your age: "))
w = float(input("Enter your weight in kg: "))
h_cm = float(input("Enter your height in cm: "))

h_m = h_cm / 100
BMI = w / (h_m**2)

x = ""
if age < 17:
    if BMI < 15:
        x += "underweight"
    elif BMI >= 15 and BMI <= 20:
        x += "normal"
    elif BMI > 20:
        x += "overweight"
if age >= 17 and age <= 35:
    if BMI < 18:
        x += "underweight"
    elif BMI >= 18 and BMI <= 24:
        x += "normal"
    elif BMI > 24:
        x += "overweight"
if age > 35:
    if BMI < 19:
        x += "underweight"
    elif BMI >= 19 and BMI <= 26:
        x += "normal"
    elif BMI > 26:
        x += "overweight"

print(f"Your body mass index (BMI) is {BMI}\nMr.{name}, you are {x}.")