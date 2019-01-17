import requests
from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
url = 'https://www.allthelyrics.com/lyrics/the_who/my_generation-lyrics-11318.html'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.title.text)
lyrics = soup.find('div', class_="content-text-inner")
stanzas = lyrics.find_all('p')
for s in stanzas:
    print(s.text)
    print('')

