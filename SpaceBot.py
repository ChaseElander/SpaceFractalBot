import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://apod.nasa.gov/apod/astropix.html'
response = requests.get(url)
html = response.content

#print html
soup = BeautifulSoup(html)
table = soup.find('img')

