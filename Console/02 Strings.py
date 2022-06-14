print("Welcome to spelling bee pro! Just submit a word:")
word = input()

upper = word.isupper()
print("The word is written in uppercase: "+ str(upper))

length = len(word)
print(word + " contains " + str(length) + " letters.")

print("First letter of " + word + " is " + str(word[0]))

print(word.replace(word,"come again?"))
