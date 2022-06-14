from matplotlib import pyplot as plt
import numpy as np
import scipy.special as sc
from math import sqrt
plt.style.use('bmh')
fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel("k", loc="right")
ax.set_ylabel("P(k)", loc="top", rotation=0)

def plot(n, p):
    x = np.arange(0, n + 1)
    y = sc.comb(n, x, exact=False) * pow(p, x) * pow(1-p, n-x)
    ax.bar(x, y)

def normal_dist(n, p):
    mu = n * p
    sigma = sqrt(n*p*(1-p))
    x = np.linspace(mu - sigma * 5, mu + sigma *5, 10**5)
    z = (x - mu) / sigma
    y = (1 / (sigma * sqrt(2*np.pi))) * pow(np.e, -0.5 * (z**2))
    ax.plot(x, y)


normal_dist(500, 0.2)
normal_dist(100, 0.4)
normal_dist(1000, 0.1)

#plot(20, 0.2)

plt.show()
