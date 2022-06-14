from functools import cache

@cache
def function(chain, n):
    for i in range(10):
        current = chain + str(i)
        if n ==9:
            print(current)
        else:
            function(current, n + 1)


function("", 0)
