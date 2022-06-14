import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

data1 = np.array([23,85, 72, 43, 52])
data2 = np.array([42, 35, 21, 16, 9])

plt.bar(range(len(data1)), data1,bottom=data1)
plt.bar(range(len(data2)), data2, bottom=data1)
plt.show()