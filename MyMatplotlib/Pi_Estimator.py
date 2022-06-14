import random as rn
from math import *
import numpy as np
num = 10**50
a = range(num)
b = range(num)
middle = (num / 2, num / 2)
outside = 0
inside = 0
for i in range(10**5):
    x = (rn.randint(0, num), rn.randint(0, num))
    distance = hypot(x[0]-middle[0], x[1]-middle[1])
    if distance <= num / 2:
        inside += 1
    outside += 1
    pi = inside * 4 / outside
    if 3.141592 < pi < 3.141593:
        print(pi)


