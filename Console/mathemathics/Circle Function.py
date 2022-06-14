import numpy
b = 6
c = 8.4
for i in numpy.arange(8,1,-1):
    print(int((50 - ((-i * i)/b))) * " " + "o" + 2 * int((20 - ((i * i)/b))) * " " + "o")
    b *= 1.2
for i in numpy.arange(1,9,1):
    print(int((50 - ((-i * i)/c))) * " " + "o" + 2 * int((20 - ((i * i)/c))) * " " + "o")
    c -= 0.6





