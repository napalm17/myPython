import requests
from bs4 import BeautifulSoup
import os

def listmaker():
    with open('watchlist_final.txt','r') as f:
        raw = f.readlines()
    watchlist = []
    for x in raw:
        watchlist.append(x[:-1])
    return watchlist

watchlist = listmaker()
print(watchlist)

def download(filmtag):
    film_title = filmtag.split('-')[0]
    url_tag = filmtag.lower().replace(' ', '-')
    print("\n" + url_tag)
    film_page = requests.get(f'https://yts.mx/movies/{url_tag}').text
    soup = BeautifulSoup(film_page, 'lxml')
    line1 = soup.find('div', class_='main-content')
    line2 = line1.find('div', class_='container', id='movie-content')
    down_link = line2.find('a', title=f"Download {film_title} 1080p.BluRay Torrent")['href']
    print(down_link)
    r = requests.get(down_link)
    with open(url_tag + '.torrent', 'wb') as f:
        f.write(r.content)
    command = "{}.torrent".format(url_tag)
    os.system(command)

failed = []

for film in watchlist:
    try:
        download(film)
    except:
        failed.append(film)
        print(failed)

with open('failed_films.txt','w') as f:
    for i in failed:
        f.writelines(i + "\n")

print(failed)


