# -*- coding: utf-8 -*-
"""
Created 5-9-20 1:23:00PM

@author: JS
"""
import bs4 
import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate


dfs = pd.read_html('https://www.nytimes.com/interactive/2020/us/pennsylvania-coronavirus-cases.html')
for df in dfs:
    print(tabulate(df, headers='keys', tablefmt='psql'))
    print(df.strip('nan'))