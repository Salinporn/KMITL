x = int(input("X: "))

import turtle
t = turtle.Turtle()
t.speed(0)


def square(x):
    for i in range(4):
        t.fd(x)
        t.rt(90)
    t.pu()


def pic(x):
    for j in range(4):
        i = 1
        while i <= 4:
            t.pd()
            square(x)
            x += x / i
            i += 1
        t.rt(90)
        x = x / 5
    turtle.done()


pic(x)
