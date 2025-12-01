# http://webscraper.io/test-sites/

import requests
from bs4 import BeautifulSoup
import pandas

# print('Request: ')
# response = requests.get('http://webscraper.io/test-sites/')
# print(response.text[:600])

# print('BeautifulSoup: ')
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify()[:600])

print('Pandas: ')
url_dado = pandas.read_csv('dados/mental_health_social_media_dataset.csv')
print(url_dado.head())