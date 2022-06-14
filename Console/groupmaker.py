import random as rn

l = [1, 2, 3, 4, 5, 6]
rn.shuffle(l)
print(l)

n = []
for i in range(0, 6, 2):
    n.append([l[i], l[i + 1]])

print(n)
