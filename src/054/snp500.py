"""
Created 6-15-20 05:20 PM
Edited Last: 6-15-20 05:20 PM

@author: JS
"""


import bs4 as bs
import pickle
import requests


def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'id': 'constituents'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.strip()
        tickers.append(ticker)


    with open ("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)


    print(tickers)
    return tickers

    
save_sp500_tickers()