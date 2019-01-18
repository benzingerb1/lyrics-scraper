import requests
from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
url = 'https://www.japanesepod101.com/lesson/lower-intermediate-lesson-4-nobody-home/?lp=134'
cookies = { 'PHPSESSID' : '', 
           'guid' : '',
           'clickpath' : '',
           '_ga' : '',
           '_gid' : '',
           '_fbp' : '',
           'guidmember' : '',
           '__atuvc' : '',
           '__atuvs' : '',
           'time_tracking' : '' }
r = requests.get(url, cookies=cookies)
soup = BeautifulSoup(r.content, 'html.parser')
print('soup is ready')
print(soup.title.text)
