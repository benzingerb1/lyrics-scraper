import requests
from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
url = 'https://www.allthelyrics.com/lyrics/the_who/my_generation-lyrics-11318.html'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.title.text)
lyrics = soup.find_all('div', class_="content-text-inner")
for l in lyrics:
	print(l.text)
