class Private:
    pay = 20000
    bonus_rate = 1000
    def __init__(self, firstname, surname, age, branch, rank, dep_time, service_year):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.branch = branch
        self.rank = rank
        self.fullname = self.firstname + " " + self.surname
        self.service_year = service_year
        self.dep_time = dep_time
    def dogtag(self):
        return self.fullname + " (" + self.age \
               + ") is a " + self.rank + " in the US " + self.branch + "."
    def services(self):
        return self.fullname + " has served in combat " + str(self.dep_time) + " times in his " \
               + str(self.service_year) + " years of service."
    def amount_pay(self):
        bonus = self.pay * (10*self.dep_time + self.service_year) / self.bonus_rate
        return self.fullname + " is paid annualy $" + str(int(self.pay + bonus))

class Corporal(Private):
    pay = Private.pay * 1.25
    bonus_rate = 800
class Sergeant(Private):
    pay = Private.pay * 1.5
    bonus_rate = 700
class Officers(Private):
    bonus_rate = 500
class Liutenant(Officers):
    pay = Private.pay * 2.25
class Captain(Officers):
    pay = Private.pay * 2.5
class Major(Officers):
    pay = Private.pay * 3
class Liutentant_Colonel(Officers):
    pay = Private.pay * 3.5
class Colonel(Officers):
    pay = Private.pay * 4
class General(Officers):
    pay = Private.pay * 5

kurtz = Colonel("Walter","Kurtz", "50", "Army", "Colonel",3 ,20 )
ryan = Private("Ryan","Johnson","25","Marine Corps", "Private",1,1)
bill = Liutentant_Colonel("William", "Killgore","40","Army","Liutenant_Colonel",2,20)
willard = Captain("Benjamin", "Willard", "30","Army", "captain",2,10)
name = bill

def interface():
    print(name.dogtag())
    print(name.amount_pay())
    print(name.services())

interface()