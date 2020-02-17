from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

url = 'https://www.mtgstocks.com/news'

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

