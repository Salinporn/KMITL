import turtle

t = turtle.Turtle()
t.speed(0)

t.fillcolor("misty rose")
t.begin_fill()
for i in range(2):
    for i in range(2):
        t.pd()
        t.fd(50)
        t.lt(90)
        t.fd(100)
        t.lt(90)
    t.pu()
    t.fd(170)
t.backward(290)
for i in range(2):
    t.pd()
    t.fd(120)
    t.lt(90)
    t.pu()
    t.fd(70)
    t.lt(90)
t.end_fill()

t.lt(90)
t.fd(70)
t.rt(90)
t.fd(25)

t.fillcolor("pink")
t.begin_fill()
for i in range(2):
    t.pd()
    t.fd(70)
    t.lt(90)
    t.fd(70)
    t.lt(90)
t.end_fill()

t.pu()
t.backward(25)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(5)
t.rt(180)

t.fillcolor("plum")
t.begin_fill()
for i in range(2):
    for i in range(3):
        t.pd()
        t.fd(60)
        t.rt(120)
    t.pu()
    t.backward(170)
t.end_fill()

t.fd(325)
t.rt(90)
t.fd(40)
t.rt(30)
t.pd()

t.fillcolor("orchid")
t.begin_fill()
for i in range(3):
    t.pd()
    t.fd(80)
    t.rt(120)
t.end_fill()

t.pu()
t.rt(150)
t.fd(140)
t.lt(90)
t.fd(20)
t.pd()

t.fillcolor("rosy brown")
t.begin_fill()
for i in range(2):
    t.fd(40)
    t.lt(90)
    t.fd(50)
    t.lt(90)
t.end_fill()

def window(size):
    t.fillcolor("rosy brown")
    t.begin_fill()
    t.circle(size)
    t.end_fill()

t.pu()
t.fd(35)
t.lt(90)
t.fd(110)
t.pd()

window(15)

t.pu()
t.rt(90)
t.fd(60)
t.rt(90)
t.fd(40)
t.pd()

window(10)

t.pu()
t.rt(90)
t.fd(150)
t.rt(90)
t.pd()

window(10)
turtle.done()