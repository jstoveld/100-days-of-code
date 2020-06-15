# -*- coding: utf-8 -*-
"""
Created 6-9-20 04:00 PM
Edited Last: 6-12-20 02:30 PM

@author: JS
"""


#Imports our required modules
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


#Dictates what style we are using to plot our dataframe
style.use('ggplot')


#Specifying the range of data we are trying to pull
start = dt.datetime(2020,1,1)
end = dt.datetime(2020,6,15)


#Specifying what stock we are pulling data on
#Using yahoo as the source of our data, and the start and end requirements from above
#Using the df.tail takes the last 5 by default but I have set it to 10 just to see what happens.
df = web.DataReader('BA', 'yahoo', start, end)

df.to_csv('BA.csv')