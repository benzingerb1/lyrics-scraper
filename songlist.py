import requests
from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
band = 'led_zeppelin'
band = 'the_who'
band = 'queen'
host = 'https://www.allthelyrics.com/' 
url = host + 'lyrics/' + band
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print('Soup is ready')
songs = []
for link in soup.select('li > a'):
    href = link.get('href')
    if href.startswith('/lyrics/' + band):
    #   f.write(href + '\n')
        songs.append(host + href)

with open(band + '.txt', 'w') as f:
    for url in songs:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        lyrics = soup.find_all('div', class_="content-text-inner")
        print(lyrics.text)
