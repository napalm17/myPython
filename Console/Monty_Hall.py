import random as rn

def execute():
    won = 0
    total = 0
    for total in range(10**5):
        sack = ["goat", "goat", "prize"]
        sack.remove(rn.choice(sack))
        sack.remove("goat")
        if sack[0] == "prize":
            won += 1
    print(round(won / total, 4))


execute()