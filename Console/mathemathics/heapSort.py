from math import *
import numpy as np
import random as rn

def swapElements(l, index1, index2):
    get = l[index1], l[index2]
    l[index2], l[index1] = get

def heapify(unsorted):
    unsorted.insert(0, 0) # start the list at position 1
    limit = floor(len(unsorted[1:]) / 2) # select all the items that have at least one node
    for i in np.arange(limit, 0, -1):
        parent, child1 = unsorted[i], unsorted[2 * i]
        try:
            child2 = unsorted[2 * i + 1]
        except IndexError:
            child2 = child1 - 1
        if child1 > parent and child1 > child2:
            swapElements(unsorted, i, 2 * i)
        elif child2 > parent:
            swapElements(unsorted, i, 2 * i + 1)
    return unsorted

def sorting(l, sorted):
    newList = heapify(l)[1:]
    maxElem, lastElem = newList.pop(0), newList.pop(-1)
    sorted.insert(0, maxElem), newList.insert(0, lastElem) # insert largest element of the list into the empty sorted list
    if len(newList) == 1:
        sorted.insert(0, newList[0])
        return None
    sorting(newList, sorted)
    return sorted

unsorted = [rn.randint(0, 100) for x in range(30)]
#unsorted = [7, 9, 2, 5, 3, 1, 8]
sorted = sorting(unsorted.copy(), [])
print("original list:    ", unsorted)
unsorted.sort()
print("sorted list:      ", sorted)
print("real sorted list: ", unsorted)
