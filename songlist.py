import requests
from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
band = 'the_who'
band = 'queen'
band = 'led_zeppelin'
host = 'https://www.allthelyrics.com/' 
url = host + 'lyrics/' + band
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
songs = []
for link in soup.select('li > a'):
    href = link.get('href')
    if href.startswith('/lyrics/' + band):
    #   f.write(href + '\n')
        songs.append(host + href)

with open(band + '.txt', 'w') as f:
    # for url in songs:
    for x in range(5):
        r = requests.get(songs[x])
        soup = BeautifulSoup(r.content, 'html.parser')
        f.write(soup.title.text)
        f.write('\n')
        lyrics = soup.find('div', class_="content-text-inner")
        stanzas = lyrics.find_all('p')
        for s in stanzas:
            f.write(s.text)
            f.write('\n\n')
        f.write('\n')

print('Soup is ready')

