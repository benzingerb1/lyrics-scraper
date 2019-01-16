import requests
from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

url = 'https://www.amazon.com/Dell-Optiplex-7010-SFF-Desktop/dp/B01HSDJFFM/ref=sr_1_3?ie=UTF8&qid=1547559117&sr=8-3&keywords=blair+technology+group'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print('Soup is ready')

