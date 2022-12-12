import turtle

r = float(input("Enter the radius of the ring: "))
t = turtle.Turtle()
t.pensize(5)

t.pencolor("blue")
t.circle(r)

t.pu()
t.fd(r/10)
t.rt(90)
t.pd()

t.pencolor("black")
t.circle(r)

t.lt(90)
t.pu()
t.fd(r+r+r/10)
t.pd()

t.pencolor("red")
t.circle(r)

t.pu()
t.fd(r/10)
t.rt(90)
t.pd()

t.pencolor("yellow")
t.circle(r)

t.lt(90)
t.pu()
t.fd(r+r+r/10)
t.pd()

t.pencolor("green")
t.circle(r)

turtle.done()