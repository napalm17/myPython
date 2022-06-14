import numpy
from math import *

dec = 1

for a in numpy.arange(pi,10*pi,0.25):
    if sin(a) > 0:
        print(100 * " " + "-" * int(pow(10,dec) * round(sin(a),dec)) + "o")
    else:
        print((100 - abs(int(pow(10, dec) * round(sin(a), dec)))) * " " + "o" + "-" * abs(int(pow(10, dec) * round(sin(a), dec))))
