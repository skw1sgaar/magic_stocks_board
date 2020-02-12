import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.mtgstocks.com/news'
response = requests.get(url)
if response.status_code != 200:
    print("Error, cannot connect to mtgstocks.com!")
