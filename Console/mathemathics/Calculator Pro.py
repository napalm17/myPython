from math import *
def calculator():
    print("Welcome to Calculator Pro!")
    while True:
        try:
            a = float(input("\nYour first number: "))
            op = input("Type of operation: ")
            b = input("Your second number: ")
            if b == "":
                b = 10
            else:
                b = float(b)
            ops = [["+", a + b], ["-", a - b], ["*", a * b], ["/", a / b],
                   ["^", pow(a, b)], ["sqrt", sqrt(a)], ["log", log(a, b)],
                   ["ln", exp(a)], ["sin", sin(a)], ["cos", cos(a)],
                   ["tan", tan(a)], ["!", factorial(int(a))]]
            for i in range(len(ops)):
                if ops[i][0] == op:
                    print("The answer is " + str(round(ops[i][1], 2)))
                    break
        except ZeroDivisionError as zer:
            print(str(zer) + ". Please enter valid values!")
        except ValueError as val:
            print(str(val) + ". Please enter valid values!")
calculator()