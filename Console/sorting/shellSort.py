from math import *
import numpy as np
import random as rn
def swapElements(l, index1, index2):
    get = l[index1], l[index2]
    l[index2], l[index1] = get


def shell(arr):
    h = len(arr) // 2
    while h >= 1:
        print(arr)
        isSorted = False
        while not isSorted:
            isSorted = True
            for i in range(len(arr) - h):
                if arr[i] > arr[i + h]:
                    swapElements(arr, i, i + h)
                    isSorted = False
            print(h)
            print(arr)
            print()
        h //= 2



arr = [7, 6, 8, 9, 3, 2, 10, 1, 5, 5, 23, 1, 6, 0, 7]
arr2 = [rn.randint(0, 100) for x in range(20)]
sorted = arr2.copy()

shell(sorted)

print()
print(arr2)
print(sorted)