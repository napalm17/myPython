n = 100

def f(n):
    total = 0
    for k in range(n):
        total += (n + 2 + (1 / n)) ** (n - 1 - k) * (n ** k)
    return (2 + (1 / n))/(n ** n) * total


print(f(n))

def f2(n):
    x = 1 / (n ** (n-1))
    a = ((n + 1) ** 2) / n
    b = n
    return x * (a ** n - b ** n)

print(f2(n))