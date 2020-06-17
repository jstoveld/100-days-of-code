"""
Created 6-15-20 05:20 PM
Edited Last: 6-16-20 10:20 AM

@author: JS
"""


import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
            pickle.dump(tickers, f)

    print(tickers)

    return tickers

save_sp500_tickers()

def get_data_from_google(reload_sp500=True):

    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
         os.makedirs('stock_dfs')

    start = dt.datetime(2000,1,1)
    end = dt.datetime(2016,12,31)

    for ticker in tickers:
        try:
            print(ticker)
            if not os.path.exists('stocks_dfs/{}.csv'.format(ticker)):
                df = web.DataReader(ticker, 'google', start, end)
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
            else:
                print('Already have {}'.format(ticker))
        except:
            print('Cannot obtain data for ' +ticker)

get_data_from_google()