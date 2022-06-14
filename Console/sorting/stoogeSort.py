from math import *
def swapElements(l, index1, index2):
    get = l[index1], l[index2]
    l[index2], l[index1] = get

def stooge(arr, l, h):
    if l >= h:
        return
    print(l, h)
    if arr[l] > arr[h]:
        swapElements(arr, l, h)
    if h - l + 1 > 2:
        t = (int)((h - l + 1) / 3)

        # Recursively sort first 2/3 elements
        stooge(arr, l, (h - t))

        # Recursively sort last 2/3 elements
        stooge(arr, l + t, (h))

        # Recursively sort first 2/3 elements
        # again to confirm
        stooge(arr, l, (h - t))
arr = [2, 4, 5, 3, 1, 9 , 0, 6, 1]
sorted = arr.copy()

stooge(sorted, 0, len(arr) - 1)

print(sorted)