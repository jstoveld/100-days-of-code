# -*- coding: utf-8 -*-
"""
Created 4-30-20 4:29:00PM

@author: JS
"""
import bs4
import requests
from bs4 import BeautifulSoup


r=requests.get('https://finance.yahoo.com/quote/FB?p=FB')
soup=bs4.BeautifulSoup(r.text, "xml")

soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})
