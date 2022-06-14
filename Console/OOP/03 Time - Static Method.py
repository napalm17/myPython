import datetime
class Time:
    def __init__(self,time):
        self.time = time
    @staticmethod
    def dayname(dayname):
        return dayname.strftime('%A')


mydate = datetime.date(2040, 1, 1)

print(Time.dayname(mydate))
