import random
class Clinic:
    my_price = 250
    my_doc = None
    docs = [["Dr. House", "Dr Chase"], ["Dr Cuddy", "Dr Wilson"], ["Dr Foreman", "Dr Hadley"]]
    branches = ["diag", "surg", "psyc"]
    hours = ["8:00","10:00","12:00","14:00","16:00"]
    def __init__(self, name, surname, is_male, branch, insurance):
        self.name = name
        self.surname = surname
        self.is_male = is_male
        self.branch = branch
        self.insurance = insurance
    def doc(self):
        for d, b in zip(Clinic.docs, Clinic.branches):
            if self.branch == b:
                Clinic.my_doc = random.choice(d)
                return Clinic.my_doc
    def price(self):
        if self.insurance:
            Clinic.my_price = Clinic.my_price * 0.5
        return Clinic.my_price
    @classmethod
    def hour(cls):
        for h in Clinic.hours:
            print(h)
    def main(self):
        gender = "Mr." if self.is_male else "Ms."
        print(gender + self.surname + ", you can have an appointment with " + Clinic.my_doc + ".\n"
              + "These are the available hours for your appointment:")
        Clinic.hour()
        my_hour = input("Select one of them: ")
        ans = input("Your total fee is $" + str(Clinic.my_price) + ", do you agree? ")
        if ans == "yes":
            Clinic.hours.remove(my_hour)
            print("Alright! Your appointment with " + Clinic.my_doc + " at " + my_hour + " is booked.")
        else:
            print("cheap ass")

def interface():
    while True:
        print("\nWelcome to House MD Clinic, please fill your personal information:")
        name = input("Your name: ")
        surname = input("Your Surname: ")
        is_male = input("Are you male: ")
        is_male = True if is_male == "yes" else False
        branch = input("Choose a branch(diag, surg or psyc): ")
        insurance = input("Do you have insurance: ")
        insurance = True if insurance == "yes" else False
        patient = Clinic(name, surname, is_male, branch, insurance)
        patient.doc()
        patient.price()
        patient.main()

interface()


#pat1 = Clinic("James" , "Corden", True, "surg", True)
#pat2 = Clinic("Hames" , "Horden", False, "diag", False)



