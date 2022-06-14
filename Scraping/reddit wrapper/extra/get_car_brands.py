from bs4 import BeautifulSoup
import requests
source = requests.get('https://www.carlogos.org/popular-car-brands/').text
soup = BeautifulSoup(source, 'lxml')
line1 = soup.find('div', class_='main')
print(soup)