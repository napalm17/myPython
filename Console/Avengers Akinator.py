def akinator():
    Avengers = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Spider-Man", "Hawkeye", "Ant-Man",
                "Scarlett Witch", "Vision"]
    print("Welcome to the Avengers Akinator. Let's find the character you chose...")
    ans1 = input("Is the character human?:")
    if ans1 == "no":
        ans1_2 = input("Is the character a nordic god?:")
        if ans1_2 == "yes":
            print("Your character is " + Avengers[2])
        else:
            print("Your character is " + Avengers[9])
    else:
        ans2 = input("Is your character a male?:")
        if ans2 == "no":
            ans2_1 = input("Was your character in the first Avengers movie?")
            if ans2_1 == "yes":
                print("Your character is " + Avengers[4])
            else:
                print("Your character is " + Avengers[8])
        else:
            ans3 = input("Was your character in the first Avengers movie?:")
            if ans3 == "no":
                ans3_1 = "Is your character a teenager"
                if ans3_1 == "yes":
                    print("Your character is " + Avengers[5])
                else:
                    print("Your character is " + Avengers[7])
            else:
                ans4 = input("Does your character have actual super strength?:")
                if ans4 == "no":
                    ans4_1 = input("Does your character have a stand-alone movie?:")
                    if ans4_1 == "yes":
                        print("Your character is " + Avengers[0])
                    else:
                        print("Your character is " + Avengers[6])
                else:
                    ans4_2 = input("Is your character a WW2 veteran?:")
                    if ans4_2 == "yes":
                        print("Your character is " + Avengers[1])
                    else:
                        print("Your character is " + Avengers[3])

akinator()
