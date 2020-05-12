# -*- coding: utf-8 -*-
"""
Created 5-11-20 3:40:00PM

@author: JS
"""
##Imports required panda and tabulate modules
import pandas as pd
from tabulate import tabulate


#Defines our function getTable that calls a URL and reads the page.
#Takes that data and defines it as dfs.
#We then take from dfs and make df and drop off the last column as it is a heatmap image.
#We then rename our columns
#Then it returns the information and tabulate formats it into a pretty chart.
def getTable():
    dfs = pd.read_html('https://www.nytimes.com/interactive/2020/us/pennsylvania-coronavirus-cases.html')
    for df in dfs:
        df.index
        df = df.drop(df.columns[-1],axis=1)
        df.rename(columns={ df.columns[0]: "PA County", df.columns[2]: "Cases per 100k people", df.columns[4]: "Deaths per 100k people" }, inplace = True)
        #return(tabulate(df, headers='keys', tablefmt='psql'))
        return(df)


#Prints our function to the console.
print(getTable())
