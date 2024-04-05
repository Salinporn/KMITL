import persistent
import ZODB, ZODB.config
from abc import ABC, abstractmethod
import datetime

class Customer(persistent.Persistent):
    def __init__(self, name=""):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self):
        return "Customer Name: " + self.name
    
    def setName(self, n):
        self.name = n

    def addAccount(self, a):
        self.accounts.append(a)
        return a
    
    def getAccounts(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None
    
    def printStatus(self):
        print(self.__str__())
        for a in self.accounts:
            print("", end="     ")
            a.printStatus()

class Account(ABC):
    def __init__(self, balance=0.0, owner=None):
        self.balance = balance
        self.owner = owner
        self.transaction = persistent.list.PersistentList()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("users must define __str__ to use this base class")
    
    def deposit(self, m):
        self.balance += m
        self.transaction.append(BankTransaction(self.balance, self.owner, m, self.balance-m, self.balance, "Deposit"))

    def withdraw(self, m):
        self.balance -= m
        self.transaction.append(BankTransaction(self.balance, self.owner, m, self.balance+m, self.balance, "Withdraw"))

    def transfer(self, m, o):
        self.transaction.append(BankTransaction(self.balance, self.owner, m, self.balance-m, self.balance, "Transfer to " + o.owner.name))
        self.balance -= m
        o.transferIn(m, self)

    def transferIn(self, m, o):
        self.transaction.append(BankTransaction(self.balance, self.owner, m, self.balance+m, self.balance, "Transfer from " + o.owner.name))
        self.balance += m
    
    def accountDetail(self):
        return self.balance, self.limit, self.interest
    
    def getBalance(self):
        return self.balance
    
    def printStatus(self):
        print(self.__str__())

    def printBankTransaction(self):
        for t in self.transaction:
            print(t)

class SavingAccount(Account, persistent.Persistent):
    def __init__(self, balance=0.0, owner=None, interest=1.0):
        Account.__init__(self, balance, owner)
        self.interest = interest

    def withdraw(self, m):
        if self.balance - m >= 0:
            super().withdraw(m)
        else:
            print("Error: Transaction failed, insufficient balance")

    def __str__(self):
        return "Saving Account of Customer : " + self.owner.name + " Balance: " + str(self.balance) + " Interest: " + str(self.interest)

class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance=0.0, owner=None, limit=-5000.0):
        Account.__init__(self, balance, owner)
        self.limit = limit

    def withdraw(self, m):
        if self.balance - m >= self.limit:
            super().withdraw(m)
        else:
            print("Error: Transaction failed, insufficient balance")

    def __str__(self):
        return "Current Account of Customer : " + self.owner.name + " Balance: " + str(self.balance) + " Limit: " + str(self.limit)
    
class BankTransaction(Account, persistent.Persistent):
    def __init__(self, balance=0.0, owner=None, amount=0.0, new_balance=0.0, old_balance=0.0, type=""):
        Account.__init__(self, balance, owner)
        self.amount = amount
        self.new_balance = new_balance
        self.old_balance = old_balance
        self.ttype = type

    def __str__(self):
        return self.ttype + "\nAmount: " + str(self.amount) + "\nOld Balance: " + str(self.old_balance) + "\nNew Balance: " + str(self.new_balance) + "\nTime Stamp: " + str(datetime.datetime.now()) + "\n"
    