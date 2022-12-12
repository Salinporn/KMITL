s = float(input("Enter your score: "))
grade = ""
if s >= 80 and s <= 100:
    grade += "A"
elif s >= 70 and s < 80:
    grade += "B"
elif s >= 60 and s < 70:
    grade += "C"
elif s >= 50 and s < 60:
    grade += "D"
elif s <= 50 and s >= 0:
    grade += "F"

print(f"Your grade: {grade}")
