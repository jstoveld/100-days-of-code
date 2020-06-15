# -*- coding: utf-8 -*-
"""
Created 6-12-20 04:00 PM
Edited Last: 6-15-20 05:20 PM

@author: JS
"""


#Imports our required modules
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')


#ma is for moving average for trend in price and smoothing of data analysis
df = pd.read_csv('BA.csv', parse_dates=True, index_col=0)
#df['100ma'] = df ['Adj Close'].rolling(window=100, min_periods=0).mean()


#Resampling of data to a more reasonable timespan (Can be min, day or sec etc)
#Mean() will shrink the dataset as it will average the value over 10 days.
#OHLC stands for open, high, low and close.
df_ohlc = df['Adj Close'].resample('5D').ohlc()
df_volume = df['Volume'].resample('5D').sum()


df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
#print(df_ohlc.head())


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()


candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

#Candlestick doesnt just want OHLC, it wants the dates in the mdates format for the OHLC
plt.show()