# -*- coding: utf-8 -*-
"""
Created 5-9-20 8:29:00AM

@author: JS
"""

import bs4 
import requests
import urllib.request
from bs4 import BeautifulSoup


source = urllib.request.urlopen('https://www.nytimes.com/interactive/2020/us/pennsylvania-coronavirus-cases.html').read()
soup = bs4.BeautifulSoup(source,'lxml')



table = soup.find('table')


table_rows = table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    converted_row = []
    for element in row:
        converted_row.append(element.strip('\n'))
        print(converted_row)
