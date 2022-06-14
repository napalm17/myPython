import numpy as np

raw = np.arange(1,31)
arr = raw.reshape(6,5)

second = raw[(raw > 1) & (raw < 21)]
third = second[0::6]

print(min(raw))
