import csv
from bs4 import BeautifulSoup
import requests

def control():
    csv_file = open('years&scores.csv', 'w')
    fields = ['year', 'score']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=",")
    csv_writer.writeheader()

        #csv_writer.writerow(['year', 'score'])
    def get_scores():
        source = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text
        soup = BeautifulSoup(source, 'lxml')
        line1 = soup.find('div', class_="lister")
        line2 = line1.find('tbody', class_="lister-list")
        for line3 in line2.find_all('tr'):
            line4 = line3.find('td', class_="titleColumn")
            year = line4.find('span').text[1:-1]
            score = line3.find('td', class_="ratingColumn imdbRating").text.replace("\n", "")
            #title = line4.find('a').text
            #print(f"{year}, {score}")
            row = {'year': year, 'score': score}
            csv_writer.writerow(row)




    #get_scores()