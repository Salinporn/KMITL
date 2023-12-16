class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def get_time(self):
        return self.hour, self.minute, self.second
    
    def print(self):
        if self.hour < 10:
            self.hour = "0" + str(self.hour)
        if self.minute < 10:
            self.minute = "0" + str(self.minute)
        if self.second < 10:
            self.second = "0" + str(self.second)
        print(f"{self.hour}:{self.minute}:{self.second} Hrs.")

time1 = Time(9, 30, 0)
time1.print()
    