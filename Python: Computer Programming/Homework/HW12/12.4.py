from abc import ABC, abstractmethod
from turtle import *

class Char(ABC):
    @abstractmethod
    def __init__(self, width):
        self.width = width

    @abstractmethod
    def draw(self, x, y):
        pass

    @abstractmethod
    def getWidth(self):
        return self.width

class Char0(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        pu()
        goto(x, y)
        seth(0)
        pd()
        for i in range(2):
            fd(super().getWidth())
            lt(90)
            fd(super().getWidth() * 1.5)
            lt(90)

    def getWidth(self):
        return self.width()


class Char1(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        pu()
        goto(x, y)
        seth(0)
        pd()
        fd(super().getWidth())
        bk(super().getWidth())
        lt(90)
        fd(super().getWidth())
        lt(135)
        fd(super().getWidth() / 2.5)

    def getWidth(self):
        return self.width()


class Char2(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        pu()
        goto(x, y)
        seth(0)
        lt(90)
        fd(super().getWidth() * 1.5)
        rt(90)
        pd()
        fd(super().getWidth())
        rt(90)
        fd(super().getWidth() * 0.75)
        rt(90)
        fd(super().getWidth())
        lt(90)
        fd(super().getWidth() * 0.75)
        lt(90)
        fd(super().getWidth())

    def getWidth(self):
        return self.width()


class Char3(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        pu()
        goto(x, y)
        seth(0)
        pd()
        fd(super().getWidth())
        lt(90)
        fd(super().getWidth() * 1.5)
        lt(90)
        fd(super().getWidth())
        pu()
        lt(90)
        fd(super().getWidth() * 0.75)
        pd()
        lt(90)
        fd(super().getWidth())

    def getWidth(self):
        return self.width()


class Char4(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        pu()
        goto(x, y)
        seth(0)
        fd(super().getWidth())
        pd()
        lt(90)
        fd(super().getWidth() * 1.5)
        bk(super().getWidth() * 0.75)
        lt(90)
        fd(super().getWidth())
        rt(90)
        fd(super().getWidth() * 0.75)

    def getWidth(self):
        return self.width()


class Char5(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        pu()
        goto(x, y)
        seth(0)
        pd()
        fd(super().getWidth())
        lt(90)
        fd(super().getWidth() * 0.75)
        lt(90)
        fd(super().getWidth())
        rt(90)
        fd(super().getWidth() * 0.75)
        rt(90)
        fd(super().getWidth())

    def getWidth(self):
        return self.width()


class Char6(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        pu()
        goto(x, y)
        seth(0)
        pd()
        for i in range(2):
            fd(super().getWidth())
            lt(90)
            fd(super().getWidth() * 0.75)
            lt(90)
        lt(90)
        fd(super().getWidth() * 1.5)
        rt(90)
        fd(super().getWidth())

    def getWidth(self):
        return self.width()


class Char7(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        pu()
        goto(x, y)
        seth(0)
        lt(90)
        fd(super().getWidth() * 1.5)
        pd()
        rt(90)
        fd(super().getWidth())
        rt(90)
        fd(super().getWidth() * 1.5)

    def getWidth(self):
        return self.width()


class Char8(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        pu()
        goto(x, y)
        seth(0)
        pd()
        for i in range(2):
            fd(super().getWidth())
            lt(90)
            fd(super().getWidth() * 1.5)
            lt(90)
        lt(90)
        fd(super().getWidth() * 0.75)
        rt(90)
        fd(super().getWidth())

    def getWidth(self):
        return self.width()


class Char9(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        pu()
        setpos(x, y)
        seth(0)
        pd()
        fd(super().getWidth())
        lt(90)
        fd(super().getWidth() * 0.75)
        for i in range(2):
            fd(super().getWidth() * 0.75)
            lt(90)
            fd(super().getWidth())
            lt(90)

    def getWidth(self):
        return self.width()


def drawNum(x):
    x = str(x)
    size = 50
    position = 0 - (len(x) * 30)
    numbers = {"0": Char0(size), "1": Char1(size),
               "2": Char2(size), "3": Char3(size),
               "4": Char4(size), "5": Char5(size),
               "6": Char6(size), "7": Char7(size),
               "8": Char8(size), "9": Char9(size)}

    for i in x:
        for key in numbers:
            if key == i:
                char = numbers[key]
                char.draw(position, 0)
                position += size * 1.25


mainloop()
