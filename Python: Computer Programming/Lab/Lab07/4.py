class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getDiscriminant(self):
        d = (self.__b ** 2) - (4 * self.__a * self.__c)
        return d

    def getRoot1(self):
        d = (self.__b ** 2) - (4 * self.__a * self.__c)
        r1 = (- self.__b + (d**(1/2)))/(2*self.__a)
        if d >= 0:
            return r1
        else:
            return 0

    def getRoot2(self):
        d = (self.__b ** 2) - (4 * self.__a * self.__c)
        r2 = (- self.__b - (d**(1/2)))/(2*self.__a)
        if d >= 0:
            return r2
        else:
            return 0

x = QuadraticEquation(1, -5, 6)
x.getDiscriminant()
x.getRoot1()
x.getRoot2()