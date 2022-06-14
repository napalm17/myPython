notes = ["C","C#","D","Eb","E","F","F#","G","G#","A","Bb","B","C","C#","D","Eb","E","F","F#","G","G#","A", "Bb", "B"]

def maj():
    print("Welome to Music Theory Calculator!")
    while True:
        root = input("Enter your root note: ")
        if root not in notes:
            print("Please enter a valid note!")
        for i in range(24):
            if root == notes[i]:
                majmin = input("Major or Minor?: ")
                if majmin == "major":
                    print("The notes of the " + root + " major chord are " + notes[i] + ", " + notes[i + 4] + " and " +
                          notes[i + 7] + ".")
                    print("The notes of the " + root + " major scale are "
                          + notes[i] + " " + notes[i + 2] + " " + notes[i + 4] + " " + notes[i + 5] + " "
                          + notes[i + 7] + " " + notes[i + 9] + " " + notes[i + 11] + " " + notes[i + 12] + ".")
                elif majmin == "minor":
                    print("The notes of the " + root + " minor chord are " + notes[i] + "," + notes[i + 3] + " and " +
                          notes[i + 7] + ".")
                    print("The notes of " + root + " minor scale are: "
                          + notes[i] + " " + notes[i + 2] + " " + notes[i + 3] + " " + notes[i + 5] + " "
                          + notes[i + 7] + " " + notes[i + 8] + " " + notes[i + 10] + " " + notes[i + 12] + ".")
                else:
                    print("Please enter either major or minor!")
                print(" ")
                break



maj()