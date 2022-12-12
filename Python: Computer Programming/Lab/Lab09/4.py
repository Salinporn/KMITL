from tkinter import *
import random
from tkinter import messagebox


class Rectangle:
    def __init__(self):
        window = Tk()
        window.title("tk")
        self.c = Canvas(window, bg="white", height=400, width=400)
        self.c.pack()
        self.c.create_rectangle(50, 50, 350, 200)
        self.c.bind("<Button-1>", self.draw)
        window.mainloop()

    def draw(self, event):
        x1, y1, x2, y2 = event.x - 3, event.y - 3, event.x + 3, event.y + 3
        colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        if 50 < event.x < 350 and 50 < event.y < 200:
            self.c.create_oval(x1, y1, x2, y2, fill=random.choice(colors))
        else:
            messagebox.showinfo("Warning", "Mouse pointer is not in the rectangle")


Rectangle()