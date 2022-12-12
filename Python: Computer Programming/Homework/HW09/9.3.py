from tkinter import *

class Circle:
    def __init__(self):
        window = Tk()
        window.title("tk")
        self.tag = 0
        self.c = Canvas(window, bg="white", height=400, width=400)
        self.c.pack()
        self.c.bind("<Button-1>", self.draw)
        self.c.bind("<Button-3>", self.remove)
        window.mainloop()

    def draw(self, event):
        x1, y1, x2, y2 = event.x - 20, event.y - 20, event.x + 20, event.y + 20
        self.c.create_oval(x1, y1, x2, y2, tags=str(self.tag))
        self.tag += 1

    def remove(self, event):
        tag = self.c.find_closest(event.x, event.y)
        self.c.delete(tag)

Circle()