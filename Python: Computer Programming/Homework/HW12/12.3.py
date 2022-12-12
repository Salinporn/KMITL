from turtle import *


class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pu()
        goto(self.x * 20, self.y * 20)
        pd()
        dot(10)

    def position(self):
        return f"{self.x}, {self.y}"


class Rectangle2D(Points):
    def __init__(self, max_x, max_y, min_x, min_y):
        super().__init__((max_x+min_x)/2, (max_y+min_y)/2)
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y

    def draw(self):
        pu()
        goto(self.min_x * 20, self.max_y * 20)
        pd()
        goto(self.max_x * 20, self.max_y * 20)
        goto(self.max_x * 20, self.min_y * 20)
        goto(self.min_x * 20, self.min_y * 20)
        goto(self.min_x * 20, self.max_y * 20)


def getRectangle(points):
    x_list = []
    y_list = []
    for xy in range(len(points)):
        if xy % 2 == 1:
            y_list += [float(points[xy])]
        elif xy % 2 == 0:
            x_list += [float(points[xy])]
    for i in range(min(len(x_list), len(y_list))):
        p = Points(x_list[i], y_list[i])
        p.draw()
        points += [p]
        p.position()
    rec = Rectangle2D(max(x_list), max(y_list), min(x_list), min(y_list))
    rec.draw()
    print(f"The bounding rectangle is centered at ({rec.position()}) with width {rec.max_x - rec.min_x} and height {rec.max_y - rec.min_y}")


def run():
    point = input("Enter the points: ").split()
    getRectangle(point)


run()
mainloop()
