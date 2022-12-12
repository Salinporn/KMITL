class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print(self):
        if self.minute <= 60 and self.second <= 60:
            print(f"{self.hour:02}:{self.minute:02}:{self.second:02} Hrs.")
        elif self.second >= 60 and self.minute >= 60:
            self.hour += (self.minute // 60)
            self.minute %= 60
            self.minute += (self.second // 60)
            self.second %= 60
            print(f"{self.hour:02}:{self.minute:02}:{self.second:02} Hrs.")
        elif self.minute >= 60:
            self.hour += (self.minute // 60)
            self.minute %= 60
            print(f"{self.hour:02}:{self.minute:02}:{self.second:02} Hrs.")
        elif self.second >= 60:
            self.minute += (self.second // 60)
            self.second %= 60
            print(f"{self.hour:02}:{self.minute:02}:{self.second:02} Hrs.")
        else:
            print("invalid")


time1 = Time(9, 30, 0)
time1.print()
