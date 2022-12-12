from abc import ABC, abstractmethod
from turtle import *

speed(0)

class TwoDShape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def draw(self):
        pu()
        goto(self.x1, self.y1)
        pd()
        goto(self.x2, self.y2)

class Rectangle(TwoDShape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def draw(self):
        pu()
        goto(self.x, self.y)
        pd()
        for i in range(2):
            fd(self.width)
            rt(90)
            fd(self.height)
            rt(90)

class Circle(TwoDShape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.radius = r

    def draw(self):
        pu()
        goto(self.x, self.y)
        pd()
        circle(self.radius)

class Square(TwoDShape):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

    def draw(self):
        pu()
        goto(self.x, self.y)
        pd()
        for i in range(4):
            fd(self.length)
            rt(90)

shape = []

try:
    trap = TwoDShape(0, 0)
    trap.draw()
except:
    print("This line should be printed")

l1 = Line(0.5, 0.6, 4.8, 9.0)
shape.append(l1)
r1 = Rectangle(10, 30, 200, 150)
shape.append(r1)
c1 = Circle(0.5, 0.6, 300)
shape.append(c1)
r2 = Rectangle(-50, 80, 300, 400)
shape.append(r2)
c2 = Circle(-20, -30, 100)
shape.append(c2)

s1 = Square(0, 0, 100)
shape.append(s1)

for s in shape:
    s.draw()

done()