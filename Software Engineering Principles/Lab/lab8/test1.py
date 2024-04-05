import ZODB, ZODB.config
import transaction
import BTrees._OOBTree
import z_obj2 as z_obj

path = "./config.xml"

db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root

if __name__ == "__main__":
    root.customers = BTrees._OOBTree.OOBTree()
    root.customers["Dave"] = z_obj.Customer("Dave")
    d = root.customers["Dave"]
    root.customers["Jone"] = z_obj.Customer("Jone")
    j = root.customers["Jone"]

    print("Create Account:")
    b1 = d.addAccount(z_obj.SavingAccount(400, d))
    b2 = j.addAccount(z_obj.CurrentAccount(200, j))
    d.printStatus()
    j.printStatus()

    print("Deposit 500 to Account 2")
    b2.deposit(500)
    b2.printStatus()

    print("Withdraw 200 from Account 1")
    b1.withdraw(200)
    b1.printStatus()

    print("Transfer 150 from Account 2 to Account 1")
    b2.transfer(150, b1)
    b1.printStatus()
    b2.printStatus()

    transaction.commit()