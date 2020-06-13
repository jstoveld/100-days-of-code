# -*- coding: utf-8 -*-
"""
Created 6-12-20 04:00 PM
Edited Last: 6-13-20 02:30 PM

@author: JS
"""


#Imports our required modules
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')


#ma is for moving average for trend in price and smoothing of data analysis
df = pd.read_csv('BA.csv', parse_dates=True, index_col=0)
df['100ma'] = df ['Adj Close'].rolling(window=100, min_periods=0).mean()
print(df.head())


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)


ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])


plt.show()