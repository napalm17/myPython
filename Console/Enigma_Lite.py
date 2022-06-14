import random
from itertools import cycle, islice
import string
l = list(string.ascii_lowercase)
l.insert(0,"0")
def enigma():
    pool = list(islice(cycle(l), 100))
    while True:
        e = random.choice(range(0,27))
        encrypted = coded = ""
        raw = input("Enter your word: ")
        for a in raw:
            for i in range(27):
                if a == pool[i]:
                    encrypted += pool[i+e]
                    #coded += str(i+e) + " "
                    break
        print(encrypted + l[e].upper()) #+ "\n" + coded)

enigma()