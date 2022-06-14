from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('scraped1.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['header', 'content', 'link'])

def basic():
    with open('simple.html', 'r') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
    # match = soup.title.text
    for article in soup.find_all('div', class_='article'):
        # print(article)
        headline = article.h2.a.text
        summary = article.p.text
        print(headline)
        print(summary)
        print()
def corey_website():
    source = requests.get('http://coreyms.com').text
    soup = BeautifulSoup(source, 'lxml')
    for article in soup.find_all('article'):
        try:
            #print(article.prettify())
            headline = article.h2.a.text
            content = article.find('div', class_='entry-content').p.text
            link = article.find('iframe', class_='youtube-player')['src']
            id = link.split('/')[4].split('?')[0]
            yt_link = f'https://youtube.com/watch?v={id}'
            #print(headline)
            #print(content)
            #print(yt_link)
        except Exception as e:
            print(str(e).upper())
        print()
        csv_writer.writerow([headline, content, yt_link])




corey_website()

csv_file.close()