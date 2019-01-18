import nltk, pprint
from nltk import word_tokenize
import requests
url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
r = requests.get(url)
tokens = word_tokenize(r.content)

