import csv
import requests
import urllib2
import shutil
import sys
import time
from BeautifulSoup import BeautifulSoup

url = 'https://apod.nasa.gov/apod/astropix.html'
response = requests.get(url)
html = response.content

print html
