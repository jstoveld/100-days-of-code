# -*- coding: utf-8 -*-
"""
Created 5-2-20 10:14:00AM
Edited Last: 5-3-20 8:14:00AM

@author: JS
"""
#Imports our required modules
import os
import sys
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
    symbol=soup.find_all('div',{'class':'D(ib) Fz(18px)'})[0].find('span').text
    
    return price, symbol


#While loop that gathers this info until the function is interupted.
#From the datetime.now we get the current time in h,m,s 
#This then prints the name and value of the symbol as well as the timestamp.
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")
    print('The current price of 'f'({stock}) ''is: $'+str(parsePrice())+' at ' +current_time)


#back to previous line sys.stdout.write("\033[F") 
#clear line sys.stdout.write("\033[K") 

## Idea - Print and clear - then if statement to print only if it changes