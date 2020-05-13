import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')


# get html using selenium webdriver, supports javascript
browser = webdriver.PhantomJS()
browser.get( "https://azure.microsoft.com/en-us/pricing/details/storage/blobs/" )
html_source = browser.page_source

# parse
soup = BeautifulSoup(html_source,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))
print(df[0].to_json(orient='records'))