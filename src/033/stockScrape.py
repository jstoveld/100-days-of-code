# -*- coding: utf-8 -*-
"""
Created 5-2-20 10:14:00 AM
Edited Last: 5-18-20 3:10:00 PM

@author: JS
"""
#Imports our required modules
from __future__ import division
import os
import sys
import time
from datetime import datetime
import bs4 
import requests
from bs4 import BeautifulSoup


#User input to request stock prices
stock = input("Please type in a stock ticker symbol to query:\n")


#Fetching the name for use later in the application
def getStockName():
    r=requests.get(f'https://finance.yahoo.com/quote/{stock}')
    soup=bs4.BeautifulSoup(r.text, "html.parser")
    name=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text 
    name = soup.text
    sep = 'Quote'
    name = name.split(sep, 1)[0]
    return name


#Definining our function getPrice that will go and look for a specific element on the below URL
#The input from the user is now converted into a literal sting with the 'f' at the start of the string. 
#User can now query the stocks they want in real time.
#Returning the current price
def getPrice():
    r=requests.get(f'https://finance.yahoo.com/quote/{stock}')
    soup=bs4.BeautifulSoup(r.text, "html.parser")
    price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    price = ' $'+price
    return price


print(getStockName(), (getPrice()))
now = datetime.now()
current_time = now.strftime("%H:%M:%S %p")
print('The current price of 'f'({stock}) ''is: $'+str(getPrice())+' at ' +current_time)


#While loop that gathers this info until the function is interupted.
#From the datetime.now we get the current time in h,m,s 
#Name and value of the symbol as well as the timestamp are printed
while True:
    newPrice = getPrice()
    time.sleep(30)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")
    currentPrice = getPrice()
    if newPrice != currentPrice:
        print('The new price of '+getStockName(), currentPrice+' at ' +current_time)
        newPrice = currentPrice
    time.sleep(30)