import math
from math import comb

sum1 = 1
sum2 = 0

for i in range(1, 10000000):
    sum1 += 1 / (2 ** i)
    print(sum1)
