class Student:
    num_of_stud = 0
    bias1 = 0.5
    bias2 = 1 - bias1
    def __init__(self, surname, lastname, first_point, second_point, is_in_team):
        self.surname = surname
        self.lastname = lastname
        self.firstpoint = first_point
        self.second_point = second_point
        self.is_in_team = is_in_team
        Student.num_of_stud += 1

    def fgrade(self):
        fgrade = ((self.firstpoint * Student.bias1) + (self.second_point * Student.bias2))
        if self.is_in_team:
            bonus = (100 - fgrade) / 2
            fgrade = fgrade + bonus
        return "The Student has a final grade of " + str(round(fgrade,2))

stud1 = Student("Chad", "Thunder",27, 43, True)
stud2 = Student("Kyle","Virgos", 87, 93, False)

#stud1.bias1 = 0.9

print(stud1.fgrade())