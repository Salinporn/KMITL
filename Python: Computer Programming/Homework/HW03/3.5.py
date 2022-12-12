import turtle

x1, y1 = input("Enter p1: ").split()
x2, y2 = input("Enter p2: ").split()
x3, y3 = input("Enter p3: ").split()

p1 = (float(x1),float(y1))
p2 = (float(x2),float(y2))
p3 = (float(x3),float(y3))

def size(a, b):
    result = ((b[0]-a[0])**2 + (b[1]-a[1])**2)**(1/2)
    return result
a = size(p1,p2)
b = size(p2,p3)
c = size(p3,p1)
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)

t = turtle.Turtle()
t.pu()
t.goto(p1)
t.pd()
t.goto(p2)
t.goto(p3)
t.goto(p1)
t.pu()

min_y = min(y1,y2,y3)
if min_y == y1:
    t.goto(p1)
elif min_y == y2:
    t.goto(p2)
else:
    t.goto(p3)
t.rt(90)
t.fd(20)
t.write(area)
t.fd(50)

turtle.done()