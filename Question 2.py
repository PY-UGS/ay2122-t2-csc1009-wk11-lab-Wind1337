class ClockTime:
    
    def setHours(self, hours):
        self.hours = hours

    def setMinutes(self, minutes):
        self.minutes = minutes

    def setSeconds(self, seconds):
        self.seconds = seconds

    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def showTime(self):
        return(self.hours + ":" + self.minutes + ":" + self.seconds)

hours = input("Input hours: ")
minutes = input("Input minutes: ")
seconds = input("Input seconds: ")

clock = ClockTime()

clock.setHours(hours)
clock.setMinutes(minutes)
clock.setSeconds(seconds)

print("Time:", clock.showTime())
