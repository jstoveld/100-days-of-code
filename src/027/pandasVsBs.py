# -*- coding: utf-8 -*-
"""
Created 5-10-20 9:50:00AM

@author: JS
"""
##Imports required modules
import pandas as pd
import requests
from bs4 import BeautifulSoup


res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))[0]
countries = df["COUNTRY"].tolist()
users = df["AMOUNT"].tolist()
 

