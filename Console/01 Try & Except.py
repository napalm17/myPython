from math import *
try:
    #a = 10 / 1
    #b = sqrt(-1)
    #c = log(1,10)
    print(int("hey"))
    #print(d)
except SyntaxError as syn:
    print(syn)
except ZeroDivisionError as zer:
    print(zer)
except ValueError as val:
    print(val)
except NameError as nam:
    print(nam)


