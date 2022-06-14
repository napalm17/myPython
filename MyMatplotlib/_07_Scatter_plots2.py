import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('ytdata.csv')

view_count = data['view_count']

likes = data['likes']
ratio = data['ratio']

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

plt.scatter(view_count, likes, edgecolor='black', linewidth=1, alpha=0.75, c=ratio, cmap='summer')

cbar = plt.colorbar()
cbar.set_label('yeah')

plt.xscale('log')
plt.yscale('log')
plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()