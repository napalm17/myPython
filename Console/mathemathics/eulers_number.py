from math import factorial, e

def eulers_number(scale=1000):
    e = 0
    for i in range(scale):
        e += 1 / factorial(i)
    return e

print(eulers_number(100000))
print(e)