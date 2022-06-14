import math

for i in range(0,1000):
    i2 = i**2
    if (i2 - 1) % 10 == 0 and (i2 - 1) % 20 != 0:
        i4 = i**4
        if i4 % 20 == 1:
            print(i)

print("END")
