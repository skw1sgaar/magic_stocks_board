import requests
import urllib.request
import time
import csv
from bs4 import BeautifulSoup

url = 'https://www.mtgstocks.com/news'
response = requests.get(url)
if response.status_code != 200:
    print("Error, cannot connect to mtgstocks.com!")
else:
    print("Connection successful!")

soup = BeautifulSoup(urllib.request.urlopen(url))

print(soup.prettify)
