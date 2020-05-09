# -*- coding: utf-8 -*-
"""
Created 5-9-20 1:23:00PM

@author: JS
"""
import bs4 
import requests
from tabulate import tabulate
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


res = requests.get('https://www.nytimes.com/interactive/2020/us/pennsylvania-coronavirus-cases.html')
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('tr')[0]
df = pd.read_html(str(table))
print( tabulate(df[0], headers='keys', tablefmt='psql') )