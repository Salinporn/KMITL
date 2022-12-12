from tkinter import *
from tkinter import messagebox

class Currency:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        self.money = IntVar()

        self.input = Entry(window, textvariable=self.money)
        self.input.pack()
        btToTHB = Button(window, text="USD -> THB", command=self.toTHB)
        btToTHB.pack()
        btToUSD = Button(window, text="THB -> USD", command=self.toUSD)
        btToUSD.pack()
        window.mainloop()

    def toTHB(self):
        self.money = int(self.input.get()) * 30
        messagebox.showinfo("USD -> THB", f"{self.input.get()} USD = {self.money:.2f} THB")

    def toUSD(self):
        self.money = int(self.input.get()) / 30
        messagebox.showinfo("THB -> USD", f"{self.input.get()} THB = {self.money:.2f} USD")


Currency()