import random

cards =["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♥", "♦", "♠", "♣"]
print("Welcome to Poker Lite!")
while True:
    input("Press ENTER to play: ")
    player = random.choice(range(len(cards)))
    comp = random.choice(range(len(cards)))

    print("You have " + cards[player] + random.choice(suits) + "."
          + "\nThe computer has " + cards[comp] + random.choice(suits) + ".")
    if player > comp:
        print("Congrats, you win!")
    elif player == comp:
        print("What are the odds... it's a draw!")
    else:
        print("Computer wins, better luck next time!")
    print(" ")

