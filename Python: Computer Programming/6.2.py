import calendar
import turtle

t = turtle.Turtle()
t.speed(0)
def calendar_of_2022(mm):
    x = 0
    s = calendar.TextCalendar(calendar.MONDAY)
    dd = {1: " Mo", 2: " Tu", 3: " We", 4: " Th", 5: " Fr", 6: " Sa", 7: " Su"}
    t.pu()
    t.lt(90)
    for j in range(2):
        t.pd()
        t.fd(20)
        t.rt(90)
        t.fd(140)
        t.rt(90)
    my = str(calendar.month_name[mm]) + " 2022"
    t.pu()
    t.rt(90)
    t.fd(35)
    t.write(my)
    t.rt(90)
    t.fd(20)
    t.lt(90)
    t.bk(35)
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
calendar_of_2022(9)
turtle.done()