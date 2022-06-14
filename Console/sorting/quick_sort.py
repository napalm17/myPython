import random as rn
import numpy as np

def long_sort(unsorted):
    while True:
        isSorted = True
        for i in range(len(unsorted)):
            try:
                a, b  = unsorted[i], unsorted[i + 1]
                if a > b:
                    unsorted.remove(a)
                    unsorted.append(a)
                    isSorted = False
            except:
                pass
        if isSorted:
            break
    print(unsorted)


def merge_sort(a):
    if len(a) == 1:
        return a
    half = int(len(a)/2)
    arr1, arr2 = a[: half], a[half:]
    #print(arr1, "and " , arr2)
    arr1, arr2 = merge_sort(arr1), merge_sort(arr2)
    return merge(arr1, arr2)


def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])
        #print(c,"#1")
    while len(a) > 0:
        c.append(a[0])
        a.remove(a[0])
        #print(c,"#2")
    while len(b) > 0:
        c.append(b[0])
        b.remove(b[0])
        #print(c,"#3")
    #print("c:", c)
    return c


x = 10**4
unsorted = [rn.randint(0,x) for i in range(x)]

sorted = merge_sort(unsorted)
print(sorted)

