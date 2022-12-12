from tkinter import *


class Painting:
    def __init__(self):
        window = Tk()
        window.title("A simple paint program")
        self.c = Canvas(window, bg="white")
        self.c.pack()
        self.c.bind("<B1-Motion>", self.draw)
        label = Label(window, text="Drag the mouse to draw")
        label.pack()
        btClear = Button(window, text="Clear", command=self.clear)
        btClear.pack()
        window.mainloop()

    def draw(self, event):
        x1, y1, x2, y2 = event.x - 3, event.y - 3, event.x + 3, event.y + 3
        self.c.create_oval(x1, y1, x2, y2, fill="#000000")

    def clear(self):
        self.c.delete("all")


Painting()