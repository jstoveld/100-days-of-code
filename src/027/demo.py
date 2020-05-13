import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import warnings
from tabulate import tabulate
warnings.filterwarnings('ignore')


# get html using selenium webdriver, supports javascript
browser = webdriver.PhantomJS()
browser.get( "https://finance.yahoo.com/quote/DIS" )
html_source = browser.page_source


# parse
soup = BeautifulSoup(html_source, 'html.parser')
price = soup.find_all('div',{'class':'D(ib) Mend(20px)'})[0].find('span').text
df = pd.read_html(str(price))
print(df)