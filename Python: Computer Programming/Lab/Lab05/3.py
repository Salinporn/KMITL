import turtle
N = int(input("N: "))
length = int(100/N)

t = turtle.Turtle()
t.speed(0)
x = 0
for i in range(N):
    for j in range(N):
        t.pu()
        t.goto(i*length,(-1)*j*length)
        t.pd()
        x = (i + j)%2
        if x == 0:
            t.fillcolor("black")
        else:
            t.fillcolor("white")
        t.begin_fill()
        for k in range(4):
            t.fd(length)
            t.rt(90)
        t.end_fill()
turtle.done()