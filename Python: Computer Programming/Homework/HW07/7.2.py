from __future__ import annotations

class Poly:
    def __init__(self, coefficient):
        self.coeffs = list(coefficient)

    def add(self, p: Poly) -> Poly:
        result = []
        for i in range(min(p.len(), self.len())):
            result.append(self.coeffs[i] + p.coeffs[i])
        for j in range(min(p.len(), self.len()), max(p.len(), self.len())):
            if p.len() > self.len():
                result.append(p.coeffs[j])
            elif p.len() < self.len():
                result.append(self.coeffs[j])
        return Poly(tuple(result))

    def scalar_multiple(self, n: int) -> Poly:
        for i in range(len(self.coeffs)):
            self.coeffs[i] *= n
        return Poly(tuple(self.coeffs))

    def multiply(self, p: Poly) -> Poly:
        result = [0] * (self.len() + p.len() - 1)
        for i in range(len(self.coeffs)):
            for j in range(p.len()):
                result[i + j] += self.coeffs[i] * p.coeffs[j]
        return Poly(tuple(result))

    def power(self, n: int) -> Poly:
        temp = Poly((self.coeffs))
        for i in range(n - 1):
            temp = temp.multiply(Poly((self.coeffs)))
        return temp

    def diff(self):
        for i in range(len(self.coeffs) - 1):
            self.coeffs[i] = self.coeffs[i + 1] * (i + 1)
        self.coeffs.pop()
        return Poly(tuple(self.coeffs))

    def integrate(self):
        for i in range(len(self.coeffs)):
            self.coeffs[i] = round(self.coeffs[i] / (i + 1), 2)
        self.coeffs.insert(0, 0.0)
        return Poly(tuple(self.coeffs))

    def eval(self, n):
        result = 0
        for i in range(len(self.coeffs)):
            result += self.coeffs[i] * int(n ** i)
        return print(result)

    def print(self):
        equation = ""
        for i in range(len(self.coeffs)):
            if self.coeffs[i] > 0:
                if i == 0:
                    equation += f"{self.coeffs[i]} "
                elif i == 1:
                    equation += f"+ {self.coeffs[i]}x "
                elif i > 0:
                    equation += f"+ {self.coeffs[i]}x^{i} "
            elif self.coeffs[i] < 0:
                if i == 0:
                    equation += f"{self.coeffs[i]} "
                elif i == 1:
                    equation += f"{self.coeffs[i]}x "
                elif i > 0:
                    equation += f"{self.coeffs[i]}x^{i} "
            else:
                pass
        print(equation)

    def len(self):
        return len(self.coeffs)

if __name__ == "__main__":
    p = Poly((1, 0, -2))
    p.print()
    q = p.power(2)
    q.print()
    p.eval(3)
    r = p.add(q)
    r.print()
    r.diff().print()