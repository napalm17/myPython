import praw
import csv
import pandas as pd

def open_txt(file):
    with open(file, 'r') as f:
        list_raw = f.read().split('\n')
    list_items = [[item, 0] for item in list_raw]
    return list_items
def control(items, subr):
    r = praw.Reddit(client_id='B_VCxIofacXrMQ', client_secret='lLMQnqrU2mpc5PkCqAnLWxJN1lGRbQ',
                         username='Jokerberkay17', password='VjBtVG2shVqyWxIc', user_agent='reddo17')
    subreddit = r.subreddit(subr)
    top = subreddit.top(time_filter="year", limit=10000)
    a = 0
    b = 0
    print("ok")
    for post in top:
        try:
            for elem in items:
                if elem[0].lower() in post.title.lower():
                    i = items.index(elem)
                    items[i][1] += 1
                    a += 1
                    print(a)
            b +=1
        except:
            pass
    print(b)
    items.sort(key=takeSecond, reverse=True)
def write_csv(items, new_file):
    with open(new_file, 'w') as csv_file:
        fields = ['item', 'mentions']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=",")
        csv_writer.writeheader()
        for elem1, elem2 in items:
            row = {'item': elem1, 'mentions': elem2}
            csv_writer.writerow(row)

def takeSecond(elem):
    return elem[1]

items = open_txt("Car_Manufacturers.txt")
control(items, "carporn")
write_csv(items, "carporn.csv")