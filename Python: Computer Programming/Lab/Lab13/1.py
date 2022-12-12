from tkinter import *
from tkinter import filedialog
import pickle


def existFile(file):
    try:
        open(file, "r")
        raise FileExistsError
    except FileNotFoundError:
        pass


class InvalidKey(BaseException):
    pass


phonebook = {}

x = input('''Phonebook Manager
Press "+" to add a new contact.
Press "-" to delete contact.
Press "f" to find a contact.
Press "s" to save all contact to a file.
Press "l" to load previous saved contact from a file.
Press "p" to print out all contacts in the phonebook.
Press "q" to quit the program.
Press: ''')

while x != "q":
    if x == "+":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        invalid = ["@", "$", "%", "^", "!"]
        try:
            for ch in name:
                if ch in invalid:
                    raise KeyError
            phonebook.update({name: phone})
        except KeyError:
            print("Invalid keywords!")
            break
    elif x == "-":
        name = input("Enter name: ")
        if name in phonebook:
            phonebook.pop(name)
        else:
            print("Name not found")
    elif x == "f":
        name = input("Enter name: ")
        if name in phonebook:
            print(phonebook[name])
        else:
            print("Name not found")
    elif x == "s":
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        filename = filedialog.asksaveasfilename(initialdir="python/lab/lab13/phonebook")
        try:
            existFile(filename)
        except FileExistsError:
            print("File already exist!")
            break
        savefile = open(filename, "wb")
        pickle.dump(phonebook, savefile)
        savefile.close()
    elif x == "l":
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        filename = filedialog.askopenfilename(initialdir="python/lab/lab13/phonebook")
        loadfile = open(filename, "rb")
        phonebook.clear()
        phonebook = pickle.load(loadfile)
        loadfile.close()
    elif x == "p":
        print(phonebook)

    x = input("Press: ")
