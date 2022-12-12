from tkinter import *


class Spinner:
    def __init__(self):
        mainWindow = Tk()
        mainWindow.title("Spinner")

        self.n = 0
        self.text = Label(mainWindow, text=self.n)
        btCountup = Button(mainWindow, text="+", command=self.increase)
        btCountdown = Button(mainWindow, text="-", command=self.decrease)
        btReset = Button(mainWindow, text="Reset", command=self.reset)
        self.text.pack()
        btCountup.pack()
        btCountdown.pack()
        btReset.pack()
        mainWindow.mainloop()

    def increase(self):
        self.n += 1
        self.text.config(text=self.n)

    def decrease(self):
        self.n -= 1
        self.text.config(text=self.n)

    def reset(self):
        self.n = 0
        self.text.config(text=self.n)

Spinner()
