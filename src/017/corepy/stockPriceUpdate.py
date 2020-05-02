# -*- coding: utf-8 -*-
"""
Created 4-30-20 4:29:00PM

@author: JS
"""
import bs4 #Imports our required modules
import requests
from bs4 import BeautifulSoup

#User input to request stock prices
stock = input("Please type in a stock ticker symbol to query:\n")

#Definining our function parsePrice that will go and look for a specific element on the below URL
#Returning the current price
def prasePrice():
    r=requests.get('https://finance.yahoo.com/quote/{stock}')
    soup=bs4.BeautifulSoup(r.text, "html.parser")
    price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

#While loop that gathers this info until the function is interupted.    
while True:
    print('the current price: '+str(prasePrice()))