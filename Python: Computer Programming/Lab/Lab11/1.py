phonebook = {}

x = input('''Phonebook Manager
Press "+" to add a new contact.
Press "-" to delete contact.
Press "f" to find a contact
Press "p" to print out all contacts in the phonebook.
Press "q" to quit the program.
Press: ''')

while x != "q":
    if x == "+":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phonebook.update({name: phone})
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
    elif x == "p":
        print(phonebook)

    x = input("Press: ")
