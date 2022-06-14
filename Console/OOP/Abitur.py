class Abitur:
    count = 1
    studs = []
    my_score = None
    def __init__(self,name, deu, eng, mat, phy, bio, che):
        self.deu = deu
        self.eng = eng
        self.mat = mat
        self.phy = phy
        self.bio = bio
        self.che = che
        self.name = name
        self.count = Abitur.count
        Abitur.studs.append(self)
        Abitur.count += 1
    def __repr__(self):
        return self.name
    def totalscore(self):
        Abitur.my_score = 2 * (self.deu + self.eng + self.mat + self.phy) + self.bio + self.che
        return Abitur.my_score
    def final(self):
        if Abitur.my_score > 140:
            return 1.0
        elif Abitur.my_score < 50:
            return "- (You have failed Abitur!)"
        for score, abi_score in zip(range(50,151,3),range(40,9,-1)):
            if Abitur.my_score <= score:
                return abi_score / 10
def interface():
    print("___Abiturnoteberechner___\n")
    for name in Abitur.studs:
        print("{}. {}:\n   Gesamtpunktzahl: {} --> Durchschnittsnote: {}\n"\
            .format(name.count, name, name.totalscore(), name.final()))

atud1 = Abitur("Berkay", 12, 13, 14, 13, 12, 12)
a = 4
stud2 = Abitur("Student", a, a, a, a, a, a)

interface()


