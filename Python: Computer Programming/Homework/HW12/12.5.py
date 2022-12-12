from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def __init__(self, goods, ppu, qty):
        self.goods = goods
        self.price = ppu
        self.qty = qty

    @abstractmethod
    def get_cost(self):
        pass


class StationaryGood(Product):
    def __init__(self, goods, ppu, qty):
        super().__init__(goods, ppu, qty)

    def get_cost(self):
        return self.price * self.qty


class Magazine(Product):
    def __init__(self, goods, ppu, qty):
        super().__init__(goods, ppu, qty)

    def get_cost(self):
        return self.price * self.qty


class Book(Product):
    def __init__(self, goods, ppu, qty):
        super().__init__(goods, ppu, qty)

    def get_cost(self):
        return self.price * self.qty * (90/100)


class Ribbon(Product):
    def __init__(self, color, length):
        super().__init__(color, 5, length)

    def get_cost(self):
        return self.price * self.qty


def getTotalCost(basket):
    total_cost = 0
    for x in basket:
        total_cost += x.get_cost()
    return f"The total cost og the goods is {total_cost:.2f} Bahts."
