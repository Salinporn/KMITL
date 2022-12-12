import turtle
import calendar

t = turtle.Turtle()
t.speed(0)
s = calendar.TextCalendar(calendar.SUNDAY)
mm = 0
x = 0
dd = {1: " Su", 2: " Mo", 3: " Tu", 4: " We", 5: " Th", 6: " Fr", 7: " Sa"}

while mm < 12:
    t.pu()
    t.goto(-400 + (150 * (mm % 6)), 300 - (200 * (1 + (mm >= 6))))
    mm += 1
    t.lt(90)
    for j in range(2):
        t.pd()
        t.fd(20)
        t.rt(90)
        t.fd(140)
        t.rt(90)
    my = " " + str(calendar.month_name[mm]) + "#" + str(mm)
    t.write(my)
    t.bk(20)
    t.rt(90)
    for k in dd:
        for _ in range(4):
            t.pd()
            t.fd(20)
            t.lt(90)
        t.write(dd[k])
        t.pu()
        t.fd(20)
    t.bk(140)
    t.rt(90)
    t.fd(20)
    t.lt(90)
    for i in s.itermonthdays(2022, mm):
        x += 1
        for _ in range(4):
            t.pd()
            t.fd(20)
            t.lt(90)
        if i != 0:
            t.pu()
            t.fd(5)
            t.write(i)
            t.bk(5)
        else:
            t.write(" ")
        if x % 7 == 0:
            t.pu()
            t.bk(120)
            t.rt(90)
            t.fd(20)
            t.lt(90)
        else:
            t.fd(20)

turtle.done()
