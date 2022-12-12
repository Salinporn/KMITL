import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def printInfo(self):
        print(f"Position: {self.x}, {self.y};")


class Circle(Point):
    def __init__(self, x, y, r=0.0):
        super().__init__(x, y)
        self.radius = float(r)

    def area(self):
        return self.radius * self.radius * math.pi

    def printInfo(self):
        print(f"Position: {self.x}, {self.y}; Radius: {self.area()};")
