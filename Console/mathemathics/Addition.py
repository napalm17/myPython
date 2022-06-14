from math import comb

def addition(minK, maxK, n, p):
    summe = 0
    try:
        for x in range(minK, maxK + 1):
            summe += comb(n, x) * pow(p, x) * pow(1 - p, n - x)
        return summe
    except OverflowError:
        return OverflowError
    except TypeError as type:
        return type


result = addition(950, 951, 6000, 1/6)
print(result)
