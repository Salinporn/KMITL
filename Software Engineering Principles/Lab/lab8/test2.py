import ZODB, ZODB.config
import transaction
import BTrees._OOBTree
import z_obj2

path = "./config.xml"

db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root

if __name__ == "__main__":
    for customer in root.customers:
        obj = root.customers[customer]
        obj.printStatus()
        print()
        index = 0
        while obj.getAccounts(index) != None:
            obj.getAccounts(index).printBankTransaction()
            print()
            index += 1