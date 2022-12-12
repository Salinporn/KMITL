class BankAccount:
    def __init__(self, bank, owner, acc_num, balance):
        self.bank = bank
        self.owner = owner
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            print("You dont have enough money")

    def print(self):
        print(f"Your current balance is {self.balance}")

m = BankAccount("ABC", "Bob", 1234, 1900)
m.deposit(100)
m.withdraw(3000)
m.print()