# import requests
import re
# import codecs
from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# url = 'https://www.amazon.com/dp/B01CV9G1BO'
# r = requests.get(url)
#txtFile = open("amz.txt.", "r")
# txtFile = codecs.open('amz.txt', encoding='utf-8')
soup = BeautifulSoup(open('amz.html'), 'html.parser')
regex = r"#\d"
for tag in soup.find_all('td'):
    tagContent = tag.text
    if bool(re.search(regex, tagContent)):
        print(tagContent)
