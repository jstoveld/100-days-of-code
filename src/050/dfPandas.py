# -*- coding: utf-8 -*-
"""
Created 6-12-20 04:00 PM
Edited Last: 6-12-20 02:30 PM

@author: JS
"""


#Imports our required modules
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')
df = pd.read_csv('BA.csv', parse_dates=True, index_col=0)


print(df[['Open', 'High']].head())
df['Adj Close'].plot()
plt.show()