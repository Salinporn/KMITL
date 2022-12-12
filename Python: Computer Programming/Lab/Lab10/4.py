import turtle
t = turtle.Turtle()
t.speed(0)


def histogram(lst):
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    freq = []
    t.goto(0, 0)
    t.fd(20)
    for num in number:
        count = lst.count(num)
        if count != 0:
            freq += [count]
            for i in range(2):
                t.fd(20)
                t.lt(90)
                t.fd(count * 20)
                t.lt(90)
            t.pu()
            t.rt(90)
            t.fd(20)
            t.write(num)
            t.bk(20)
            t.lt(90)
            t.pd()
            t.fd(20)
        else:
            pass

    t.fd(20)
    t.pu()
    t.write("X")
    t.goto(0, 0)
    t.pd()
    t.lt(90)
    t.fd(max(freq) * 20)
    t.write("Y")
    t.hideturtle()
    turtle.done()


histogram([1, 2, 2, 1, 3, 4, 6, 5, 6, 4, 3, 5, 4, 5, 3, 5, 7])