import turtle
t = turtle.Turtle()
t.speed(0)


def cross(x, y):
    if y >= 0:
        for i in range(4):
            t.fd(x)
            if y != 1:
                cross(x / 2, y - 1)
            else:
                t.dot(6)
            t.fd(x * -1)
            t.lt(90)
    else:
        t.dot(6)


cross(100, 3)

turtle.done()
