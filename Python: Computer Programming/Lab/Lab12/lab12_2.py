class Calculator:
    def __init__(self, acc=0.0):
        self.acc = float(acc)

    def set_accumulator(self, a):
        self.acc = a

    def get_accumulator(self):
        return self.acc

    def add(self, x):
        self.acc += x
        return self.acc

    def subtract(self, x):
        self.acc -= x
        return self.acc

    def multiply(self, x):
        self.acc *= x
        return self.acc

    def divide(self, x):
        if x != 0:
            self.acc /= x
            return self.acc

    def print_result(self):
        print(f"Result: {self.acc}")


class Sci_cal(Calculator):
    def __init__(self):
        super().__init__()

    def square(self):
        self.acc *= self.acc
        return self.acc

    def exp(self, x):
        self.acc = self.acc ** x
        return self.acc

    def factorial(self):
        fact = 1
        for i in range(1, self.acc + 1):
            fact = fact * i
        self.acc = fact
        return self.acc

    def print_result(self):
        print(f"Result: {self.acc:.2e}")