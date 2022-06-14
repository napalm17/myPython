from bs4 import BeautifulSoup
import requests


def get_symbols():
    url = 'https://en.wikipedia.org/wiki/NASDAQ-100'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    #print(soup.prettify())
    line1 = soup.find('table', id="constituents")
    list_symbols = []
    for i in line1.find_all('td'):
        if i.text.isupper():
            print(i.text)
            list_symbols.append(i.text)
    with open('symbols.txt', 'w') as f:
        for x in list_symbols:
            f.writelines(x)
get_symbols()