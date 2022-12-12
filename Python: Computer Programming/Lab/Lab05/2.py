import turtle
N = int(input("N: "))
length = int(100/N)

t = turtle.Turtle()
# t.speed(0)
for i in range(N+1):
    t.pd()
    t.fd(length*N)
    t.pu()
    t.bk(length*N)
    t.rt(90)
    t.fd(length)
    t.lt(90)
t.pu()
t.lt(90)
t.fd(length)
for j in range(N+1):
    t.pd()
    t.fd(length * N)
    t.pu()
    t.bk(length * N)
    t.rt(90)
    t.fd(length)
    t.lt(90)

turtle.done()