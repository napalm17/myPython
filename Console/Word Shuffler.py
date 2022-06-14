import random
while True:
    word = input("Enter the word you want to shuffle: ")
    l = list(word)
    random.shuffle(l)
    print("".join(l))