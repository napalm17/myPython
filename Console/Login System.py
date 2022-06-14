realnick = "dude"
orpass = "dudism"
def login():
    while True:
        nick = input("Username:")
        passw = input("Password:")
        if nick == realnick and passw == orpass:
            print("You are now logged in. Have fun surfing on TikTok!")
            break
        else:
            print("Your password is incorrect. Would you like to... \n a) Try again \n b) Reset your password")
            ans = input("a or b:")
            if ans == "a":
                continue
            elif ans == "b":
                while True:
                    ans2_1 = input("Enter the name of your first pet:")
                    ans2_2 = input("Enter the city you were born in:")
                    if ans2_1 == "rocky" and ans2_2 == "van":
                        print("Good!")
                        while True:
                            ans3 = input("Please enter your new password:")
                            if ans3 == "marcus":
                                print("Your new password cannot be the same as your old password!")
                            else:
                                realpassw = ans3
                                print("Your password was reset successfully.")
                                break
                        break
                    else:
                        print("Incorrect, would you like to... \n a) try again: \n b) Go back to the Login page")
                        ans4 = input("a or b:")
                        if ans4 == "a":
                            continue
                        elif ans4 == "b":
                            break
            else:
                print("Please enter a valid operation!:")
                continue
        break
def register():
    while True:
        realnick = input("Choose your username:")
        orpass = input("Choose a strong password:")
        if len(orpass) < 5:
            print("Your password is weak!")
        elif realnick == "dude":
            print("That username is already taken!")
        else:
            print("Good, now you can login.")
            login()
            break
while True:
    ans0 = input("Welcome to TikTok! Would you like to...\n a) Register or b) Login:")
    if ans0 == "b":
        login()
        break
    elif ans0 == "a":
        register()
        break















