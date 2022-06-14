from math import sqrt

def a(n):
    if n == 0:
        return sqrt(1 + n)
    else:
        return sqrt(1 + a(n - 1))


result = a(100)
print(result)

print((1+sqrt(5))/2)
math.i