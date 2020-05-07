# -*- coding: utf-8 -*-
"""
Created 5-2-20 10:14:00AM
Edited Last: 5-6-20 1:12:00PM

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

#Definining our function parsePrice that will go and look for a specific element on the below URL
#The input from the user is now converted into a literal sting with the 'f' at the start of the string. 
#User can now query the stocks they want in real time.
#Returning the current price
def parsePrice():
    r=requests.get(f'https://finance.yahoo.com/quote/{stock}')
    soup=bs4.BeautifulSoup(r.text, "html.parser")
    price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price


def price_change(current, previous):
    if (previous != 0):
        return (abs(current - previous) / previous) * 100.0


previous_price = 0
now = datetime.now()
current_time = now.strftime("%H:%M:%S %p")
print('The current price of 'f'({stock}) ''is: $'+str(parsePrice())+' at ' +current_time)


#While loop that gathers this info until the function is interupted.
#From the datetime.now we get the current time in h,m,s 
#Name and value of the symbol as well as the timestamp are printed
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")
    current_price = parsePrice()
    if previous_price != current_price:
        print('PRICE CHANGE! 'f'({stock}) '+(price_change(current_price, previous_price))+'% '' is: $'+current_price+' at ' +current_time)
        previous_price = current_price
    time.sleep(70)