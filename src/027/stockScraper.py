# -*- coding: utf-8 -*-
"""
Created 5-10-20 12:50:00PM

@author: JS
"""
##Imports required modules
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


stock = input("Please type in a stock ticker symbol to query:\n")


def getPrice():
    res = requests.get(f'https://finance.yahoo.com/quote/{stock}')
    soup = BeautifulSoup(res.content,'lxml')
    price = soup.find_all('span')[0] 
    df = pd.read_html(str(price))
    return(df)

print(getPrice())
