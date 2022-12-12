import math
import turtle
t = turtle.Turtle()

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def getArea(self):
        area = math.pi * self.r * self.r
        return area

    def getPerimeter(self):
        perimeter = math.pi * self.r * 2
        return perimeter

    def move(self, newX, newY):
        self.x = newX
        self.y = newY

    def draw(self):
        t.pu()
        t.goto(self.x, self.y)
        t.rt(90)
        t.fd(self.r)
        t.lt(90)
        t.pd()
        t.circle(self.r)

a = Circle(0, 0, 100)
a.getArea()
a.getPerimeter()
a.draw()
a.move(50, 50)
a.draw()
turtle.done()