text = input("Enter some text: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"

import turtle

t = turtle.Turtle()
c = t.clone()
t.goto(0, 0)
t.fd(20)

freq = []
for ch in alphabet:
    count = text.count(ch)
    if count != 0:
        freq += [count]
        for i in range(2):
            t.fd(10)
            t.lt(90)
            t.fd(count * 20)
            t.lt(90)
        t.pu()
        t.rt(90)
        t.fd(20)
        t.write(ch)
        t.bk(20)
        t.lt(90)
        t.pd()
        t.fd(30)
    else:
        pass

c.pu()
c.goto(0, 0)
c.pd()
c.lt(90)
c.fd(max(freq) * 20)

turtle.done()
