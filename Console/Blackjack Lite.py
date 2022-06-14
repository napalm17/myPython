import random
high = 0
while True:
    input("Press ENTER to play: ")
    c1 = random.choice(range(1,11))
    c2 = random.choice(range(1,11))
    print("Your cards are " + str(c1) + " and " + str(c2) + ".")
    d = c1 + c2
    while d <= 21:
        ans1 = input("\nWould you like another card?(a for yes, b for no): ")
        if ans1 == "a":
            c3 = random.choice(range(1, 11))
            d += c3
            print("Your new card is " + str(c3) + " (The sum is " + str(d) + ").")
            if d > 21:
                print("You exceeded 21... Better luck next time!")
                break
        elif ans1 == "b":
            print("Alright! You have won " + str(d) + " points." )
            if d > high:
                high = d
                print("Congrats, " + str(d) + " is your new high score!")
            break
    print(" ")