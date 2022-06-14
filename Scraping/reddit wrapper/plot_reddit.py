import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import random as rn

def rgb():
    rgb = []
    for i in range(3):
        rgb.append(rn.randint(0, 7) / 10)
    rgb.append(1)
    return rgb
def plotting(csv_file):
    data = pd.read_csv(csv_file)
    items, mentions = np.array(data['item']), np.array(data['mentions'])
    i = 21
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot()
    colors = [rgb() for x in range(len(items))]
    ax.barh(items[:i], mentions[:i], align='center', color=colors, edgecolor="k", lw="0.1")
    ax.set_xlabel("Popularity (according to " + csv_file[:-4].replace("_", "/") + ")")
    ax.invert_yaxis()
    plt.tight_layout()
    fig.savefig(csv_file[:-4] + "2.png")
def control():
    plotting('r_jazz.csv')
    plotting('r_progrockmusic.csv')
    plotting('r_cityporn.csv')
    plotting('r_carporn.csv')

#control()

