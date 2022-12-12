import turtle
import random
t = turtle.Turtle()
t.speed(0)

def pie_chart(lst):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    freq = []
    for i in numbers:
        count = lst.count(i)
        if count != 0:
            freq += [count]
            degree = (count/len(lst))*360
            colors = ["blue", "brown", "red", "yellow", "green", "orange", "beige", "turquoise", "pink"]
            t.fillcolor(random.choice(colors))
            t.begin_fill()
            t.lt(90)
            t.forward(100)
            t.rt(90)
            t.circle(-100, degree)
            t.rt(90)
            t.fd(100)
            t.end_fill()
            t.lt(90)
    t.hideturtle()
    turtle.done()


pie_chart([3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3])
