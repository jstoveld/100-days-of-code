# -*- coding: utf-8 -*-
"""
Created 5-11-20 6:40:00PM

@author: JS
"""
##Imports required panda and tabulate modules
from __future__ import division
import pandas as pd
import os
import sys
import time
from datetime import datetime


stock = input("Please type in a stock ticker symbol to query:\n")


def getPrice():
    dfs = pd.read_html(f'https://finance.yahoo.com/quote/{stock}')
    for df in dfs:
        return(df)


previous_price = 0
current_price = getPrice()


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")
    current_price = getPrice()
    if previous_price != current_price:
        print('PRICE CHANGE! 'f'({stock})'+str(current_price, previous_price)+'% '' is: $'+current_price+' at ' +current_time)
    previous_price = current_price
    time.sleep(70)