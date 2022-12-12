import turtle
import math

r = float(input("radius: "))
area = math.pi * r * r

t = turtle.Turtle()
t.circle(r)
t.pu()
t.lt(90)
t.fd(r)

t.write(area)

turtle.done()