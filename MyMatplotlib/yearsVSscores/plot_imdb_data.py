import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv('years&scores.csv')
years = np.array(data['year'])
scores = np.array(data['score'])
years2 = []
scores2 = []
for a, b in zip(years, scores):
    if a not in years2:
        years2.append(a)
        scores2.append([b, 1])
    else:
        i = years2.index(a)
        scores2[i][0] += b
        scores2[i][1] += 1

def takeFirst(elem):
    return elem[0]

raw = [(x, y) for x, y in zip(years2, scores2)]
raw.sort(key=takeFirst)
final_year, final_score, amount = [x for x, y in raw], [y[0] / y[1] for x, y in raw], [y[1] for x, y in raw]

def plotting():
    fig = plt.figure(figsize=(10, 6))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.scatter(years, scores, lw=1, edgecolor="k", alpha=0.75, color="yellow", s=20)
    ax1.plot(final_year, final_score, lw=0.75, color="k")
    ax2.bar(final_year, amount, alpha=0.5)
    ax1.set_title('ImdB Scores In Relation To Years')
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Score")
    plt.tight_layout()
    plt.show()
plotting()