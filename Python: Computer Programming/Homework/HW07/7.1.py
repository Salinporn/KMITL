import datetime
current_time = datetime.datetime.now()


class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def setTime(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def getTime(self):
        self.hour = current_time.hour
        self.minute = current_time.minute
        self.second = current_time.second

    def tick(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0

    def display(self):
        if self.minute < 60 and self.second < 60:
            ampm = ""
            if 0 <= self.hour < 12:
                ampm += "AM"
                print(f"{self.hour:02}:{self.minute:02}:{self.second:02} {ampm}")
            elif 12 <= self.hour < 24:
                ampm += "PM"
                print(f"{self.hour:02}:{self.minute:02}:{self.second:02} {ampm}")
            else:
                print("invalid")
        else:
            print("invalid")


time = Clock(23, 8, 40)
# time.setTime(8, 0, 0)
time.tick()
time.getTime()
time.display()
