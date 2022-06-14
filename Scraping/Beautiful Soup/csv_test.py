import csv
import pandas as pd

list_results = ['False, 60, 40 ', 'True, 70, 30, ']

def f():
    with open('example35.csv', 'w') as result:
        writer = csv.writer(result, delimiter=",")
        writer.writerow(('Correct?', 'Successes', 'Failures'))
        for row in list_results:
            columns = [c.strip() for c in row.strip(', ').split(',')]
            writer.writerow(columns)
f()
df = pd.read_csv("example35.csv")
print(df)