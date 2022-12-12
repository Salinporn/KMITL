import turtle

l = float(input("Enter the length of the star: "))

t = turtle.Turtle()
for i in range(5):
    t.fd(l)
    t.rt(144)
turtle.done()