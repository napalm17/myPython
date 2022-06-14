import random
symbols = ["🍇","🍉","🍓","🍀","🍒","🍑"]
while True:
    input("Press ENTER to play: ")
    s1 = random.choice(symbols)
    s2 = random.choice(symbols)
    s3 = random.choice(symbols)
    print(s1 + s2 + s3)

    if s1 == s2 == s3:
        print("Congrats, you win!")
    else:
        print("Better luck next time")
    print(" ")