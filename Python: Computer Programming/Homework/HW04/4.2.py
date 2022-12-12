import turtle

x1, y1 = map(float, input("Enter center of rectangle1: ").strip("(").strip(")").split(","))
w1 = float(input("Enter the width: "))
h1 = float(input("Enter the height: "))
x2, y2 = map(float, input("Enter center of rectangle2: ").strip("(").strip(")").split(","))
w2 = float(input("Enter the width: "))
h2 = float(input("Enter the height: "))

#Rectangle = [bottomleft_x, bottomleft_y, topright_x, topright_y]
R1 = [x1-(w1/2), y1-(h1/2), x1+(w1/2), y1+(h1/2)]
R2 = [x2-(w2/2), y2-(h2/2), x2+(w2/2), y2+(h2/2)]

if (R1[0]<R2[0]) and (R1[1]<R2[1]) and (R1[2]>R2[2]) and (R1[3]>R2[3]):
    print("Rectangle2 is inside Rectangle1")
elif (R1[0]>R2[0]) and (R1[1]>R2[1]) and (R1[2]<R2[2]) and (R1[3]<R2[3]):
    print("Rectangle1 is inside Rectangle2")
elif (R1[0]>R2[0]) and (R1[1]>R2[1]) and (R1[2]>R2[2]) and (R1[3]<R2[3]):
    print("overlap")
elif R1[0]>=R2[2] or R1[2]<=R2[0] or R1[3]<=R2[1] or R1[1]>=R2[3]:
    print("not overlap")
else:
    print("overlap")

t = turtle.Turtle()
t.pu()
t.goto(R1[0],R1[1])
t.pd()
t.lt(90)
t.fd(h1)
t.rt(90)
t.fd(w1)
t.rt(90)
t.fd(h1)
t.rt(90)
t.fd(w1)

t.pu()
t.goto(R2[0],R2[1])
t.pd()
t.rt(90)
t.fd(h2)
t.rt(90)
t.fd(w2)
t.rt(90)
t.fd(h2)
t.rt(90)
t.fd(w2)
turtle.done()