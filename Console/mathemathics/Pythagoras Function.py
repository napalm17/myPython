from math import *
import nameof
def pyth():
    while True:
        try:
            a = input("\nEnter the length of one of the triangle's legs: ")
            b = input("Enter the length of the other leg of the triangle: ")
            c = input("Enter the length of the triangle's hypotenuse: ")
            if c == "?":
                result = round(sqrt(pow(int(a),2) + pow(int(b),2)),2)
                print("Hypotenuse of this triangle is " + str(result) + " units of length")

            elif a == "?":
                    result = round(sqrt(pow(int(c),2) - pow(int(b),2)),2)
                    print("The missing leg of this triangle is " + str(result) + " units of length")

            elif b == "?":
                    result = round(sqrt(pow(int(c),2) - pow(int(a),2)),2)
                    print("The missing leg of this triangle is " + str(result) + " units of length")
        except:
            print("Please enter valid values!")
pyth()