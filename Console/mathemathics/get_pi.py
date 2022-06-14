import numpy as np
from math import sqrt
def generate_pi(x):
    total = 0
    for i in range(1, x):
        total += 1 / (i**2)
    return sqrt(6 * total)

myPi = generate_pi(10**5)
print(myPi)
print(np.pi)
