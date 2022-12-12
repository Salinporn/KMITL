import turtle

x = int(input("size: "))

t = turtle.Turtle()
h = x/6
w = 1.5 * x

t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
for i in range(2):
    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.rt(90)
t.end_fill()

t.pu()
t.rt(90)
t.fd(h)
t.lt(90)
t.pd()

t.fillcolor("blue")
t.begin_fill()
for i in range(2):
    t.fd(w)
    t.rt(90)
    t.fd(2*h)
    t.rt(90)
t.end_fill()

t.pu()
t.rt(90)
t.fd(2*h)
t.lt(90)
t.pd()

t.fillcolor("white")
t.begin_fill()
for i in range(2):
    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.rt(90)
t.end_fill()

t.pu()
t.rt(90)
t.fd(h)
t.lt(90)
t.pd()

t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.rt(90)
t.end_fill()

turtle.done()