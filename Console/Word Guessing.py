import random
while True:
    def hashing():
        ori = word = "kendrick"
        hash = ""
        input("\nPress Enter to play:")
        for i in range(len(word)):
            if len(word) > 0:
                a = random.choice(word)
                hash += a
                word = word.replace(a,"")
            else:
                print(hash)
                break
        for x in range(3):
            ans = input("Guess the word:")
            if ans == ori:
                print("Congrats! The word was " + ori + ".")
                break
            elif ans!= ori and x == 2:
                print("You are out of guesses.")
                break
            else:
                print("Wrong!")
    hashing()

