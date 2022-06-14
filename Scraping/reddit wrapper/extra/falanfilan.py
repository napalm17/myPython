import pandas as pd

data = pd.read_csv('cities_data.csv')
cities = list(data['Name'])

print(cities)

with open('cities.txt', 'w') as f:
    for i in cities:
        f.write(i + '\n')