import tkinter as tk
from tkinter import messagebox


class MobilePhone:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("KMITL Phone")

        self.input = tk.Entry(self.window, justify="right")
        self.input.grid(row=0, sticky="N", padx=11, pady=5)

        self.onebt = tk.Button(self.window, text="1", width=5, height=2, command=lambda: self.displaytext(1))
        self.onebt.grid(row=1, sticky="W")

        self.twobt = tk.Button(self.window, text="2", width=5, height=2, command=lambda: self.displaytext(2))
        self.twobt.grid(row=1)

        self.threebt = tk.Button(self.window, text="3", width=5, height=2, command=lambda: self.displaytext(3))
        self.threebt.grid(row=1, sticky="E")

        self.fourbt = tk.Button(self.window, text="4", width=5, height=2, command=lambda: self.displaytext(4))
        self.fourbt.grid(row=2, sticky="W")

        self.fivebt = tk.Button(self.window, text="5", width=5, height=2, command=lambda: self.displaytext(5))
        self.fivebt.grid(row=2)

        self.sixbt = tk.Button(self.window, text="6", width=5, height=2, command=lambda: self.displaytext(6))
        self.sixbt.grid(row=2, sticky="E")

        self.sevenbt = tk.Button(self.window, text="7", width=5, height=2, command=lambda: self.displaytext(7))
        self.sevenbt.grid(row=3, sticky="W")

        self.eightbt = tk.Button(self.window, text="8", width=5, height=2, command=lambda: self.displaytext(8))
        self.eightbt.grid(row=3)

        self.ninebt = tk.Button(self.window, text="9", width=5, height=2, command=lambda: self.displaytext(9))
        self.ninebt.grid(row=3, sticky="E")

        self.zerobt = tk.Button(self.window, text="0", width=5, height=2, command=lambda: self.displaytext(0))
        self.zerobt.grid(row=4)

        self.starbt = tk.Button(self.window, text="*", width=5, height=2, command=lambda: self.displaytext("*"))
        self.starbt.grid(row=4, sticky="W")

        self.squarebt = tk.Button(self.window, text="#", width=5, height=2, command=lambda: self.displaytext("#"))
        self.squarebt.grid(row=4, sticky="E")

        self.talk = tk.Button(self.window, text="Talk", width=9, height=2, command=self.talk)
        self.talk.grid(row=5, sticky="WS")

        self.delete = tk.Button(self.window, text="<", width=9, height=2, command=self.deletechar)
        self.delete.grid(row=5, sticky="SE")

        self.window.mainloop()

    def displaytext(self, char):
        self.input.insert(len(self.input.get()), char)

    def talk(self):
        messagebox.showinfo("Dial", f"Dialing <<{self.input.get()}>>")

    def deletechar(self):
        self.input.delete(len(self.input.get())-1, len(self.input.get()))

MobilePhone()
