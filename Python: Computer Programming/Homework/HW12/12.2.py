import turtle


def RobotBattle():
    robotList = []

    while True:
        turtle.clear()
        for robot in robotList:
            robot.draw()
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, " : ")
            robot.displayStatus()
            i += 1
        print("================")

        choice = input("Enter which type of robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robot to create")
            robotType = input("'r' for Robot, 'm' for Medicbot, 's' for StrikerBot: ")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)

        i = 0
        for robot in robotList:
            if robot.health <= 0:
                del robotList[i]
            i += 1

class Robot(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.health = 100
        self.energy = 100

    def move(self, x, y):
        if self.energy > 0:
            self.x = x
            self.y = y
            self.energy -= 10
        else:
            print("error")

    def draw(self):
        turtle.pu()
        turtle.goto(self.x, self.y)
        turtle.rt(90)
        turtle.fd(15)
        turtle.lt(90)
        turtle.pd()
        turtle.fillcolor("#FFFAFA")
        turtle.begin_fill()
        turtle.circle(15)
        turtle.end_fill()

    def displayStatus(self):
        print(f"x = {self.x}\ty = {self.y}\nhealth = {self.health}\nenergy = {self.energy}")

    def command(self, robotList):
        print("Possible actions: move")
        newx = int(input("Enter new X coordinate: "))
        newy = int(input("Enter new Y coordinate: "))
        self.move(newx, newy)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()

    def heal(self, r):
        if self.energy >= 20 and (((self.x - r.x)**2 + (self.y - r.x)**2)**(1/2)) <= 10:
            self.energy -= 20
            r.health += 10
        else:
            print("error")

    def command(self, robotList):
        cm = input("Enter 'move' to move the robot or 'heal' to heal other robot in robotList: ")
        if cm == "move":
            newx = int(input("Enter new X coordinate: "))
            newy = int(input("Enter new Y coordinate: "))
            self.move(newx, newy)
        elif cm == "heal":
            robot = input("Enter robot in robotList you want to heal: ")
            self.heal(robotList[robot])
        else:
            print("error")

    def draw(self):
        super().draw()
        turtle.pencolor("#FF82AB")
        turtle.pensize(5)
        turtle.lt(90)
        turtle.pu()
        turtle.fd(8)
        turtle.pd()
        turtle.fd(14)
        turtle.pu()
        turtle.fd(8)
        turtle.bk(15)
        turtle.rt(90)
        turtle.bk(15)
        turtle.fd(8)
        turtle.pd()
        turtle.fd(14)
        turtle.pu()
        turtle.fd(8)
        turtle.pencolor("black")
        turtle.pensize(1)

class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5

    def strike(self, r):
        if self.energy >= 20 and self.missile > 0 and (((self.x - r.x)**2 + (self.y - r.x)**2)**(1/2)) <= 10:
            self.energy -= 20
            self.missile -= 1
            r.health -= 50
        else:
            print("error")

    def displayStatus(self):
        print(f"x = {self.x}\ty = {self.y}\nhealth = {self.health}\nenergy = {self.energy}\nmissile = {self.missile}")

    def command(self, robotList):
        cm = input("Enter 'move' to move the robot or 'strike' to strike other robot in robotList: ")
        if cm == "move":
            newx = int(input("Enter new X coordinate: "))
            newy = int(input("Enter new Y coordinate: "))
            self.move(newx, newy)
        elif cm == "strike":
            robot = input("Enter robot in robotList you want to strike: ")
            self.strike(robotList[robot])
        else:
            print("error")

    def draw(self):
        super().draw()
        turtle.pu()
        turtle.pencolor("#03A89E")
        turtle.lt(90)
        turtle.fd(7)
        turtle.pd()
        turtle.rt(90)
        turtle.fillcolor("#03A89E")
        turtle.begin_fill()
        turtle.circle(8, 360, 4)
        turtle.end_fill()
        turtle.pencolor("black")

RobotBattle()