# -*- coding: utf-8 -*-
"""
Created 5-2-20 10:14:00 AM
Edited Last: 6-2-20 3:21:00 PM

@author: JS
"""


#Imports our required modules
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
    return price


#This gets what the time is right now and prints out what the stock is valued at
#Concatinating the text (str) and the value as well as the stock name and current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S %p")
print('The current price of '+str(getStockName())+ 'is: $'+str(getPrice())+' at ' +current_time)


#Check price calls again in 30 seconds to get the price again
#This will give us something to compare getPrice to for later in our code.
def priceCheck():
    #time.sleep(30)
    r=requests.get(f'https://finance.yahoo.com/quote/{stock}')
    soup=bs4.BeautifulSoup(r.text, "html.parser")
    price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price


def originalPrice():
    originalPrice=float(getPrice())
    return originalPrice


while True:
    def priceChangePercent():
        oldPrice = (originalPrice())
        newPrice = float(priceCheck())
        priceChange = ((oldPrice - newPrice) / newPrice * 100.0)
        return round(priceChange)


    if priceChangePercent() != 0:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S %p")
        print((str(round(priceChangePercent(), 2))+' % ''The current price of '+str(getStockName())+ 'is: $'+str(getPrice())+' as of ' +current_time))
        priceChange = 0
        
    else:
        time.sleep(50)