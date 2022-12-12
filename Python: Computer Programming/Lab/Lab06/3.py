import turtle

t = turtle.Turtle()


def draw_polygon(x, y, numberofside=4, size=100):
    t.pu()
    t.goto(x, y)
    t.pd()
    for _ in range(int(numberofside)):
        turtle.forward(int(size))
        turtle.right(360 / int(numberofside))


draw_polygon(0, 0)
turtle.done()
