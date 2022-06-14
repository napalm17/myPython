def gcdlcm():
    print("Welcome to GCD and LCD calculator! Please enter your...")
    a = int(input("First Number:"))
    b = int(input("Second Number:"))

    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            print("GCD of " + str(a) + " and " + str(b) + " is " + str(i) + ".")
            break
    for i in range(a, a*b+1, 1):
        if i % a == 0 and i % b == 0:
            print("LCM of " + str(a) + " and " + str(b) + " is " + str(i) + ".")
            break
gcdlcm()