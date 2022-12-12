import turtle

x0, y0 = map(float, input("Enter p0: ").strip("(").strip(")").split(","))
x1, y1 = map(float, input("Enter p1: ").strip("(").strip(")").split(","))
x2, y2 = map(float, input("Enter p2: ").strip("(").strip(")").split(","))

m = (y1 - y0)/(x1 - x0)
y = (m*(x2-x0)) + y0

position = ""
if m > 0:
    if y2 < y:
        position += "on the right side of "
    elif y2 > y:
        position += "on the left side of "
    else:
        position += "on the "
elif m < 0:
    if y2 < y:
        position += "on the left side of "
    elif y2 > y:
        position += "on the right side of "
    else:
        position += "on the "
elif m == 0:
    if y2 < y:
        position += "below "
    elif y2 > y:
        position += "above "
    else:
        position += "on the "

print(f"p2 is {position}the line between p0 and p1.")

p0 = (float(x0), float(y0))
p1 = (float(x1), float(y1))
p2 = (float(x2), float(y2))

# check with turtle
t = turtle.Turtle()
t.pu()
t.goto(p0)
t.pd()
t.goto(p1)
t.pu()
t.goto(p2)
t.pd()
t.dot(3)
t.hideturtle()
turtle.done()
