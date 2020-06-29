from collections import Counter
import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from tabulate import tabulate
from warnings import filterwarnings
filterwarnings('ignore')

def process_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)
    
    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]
        
    df.fillna(0, inplace=True)
    return tickers, df

def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return "BUY"
        if col < -requirement:
            return "SELL"
    return "HOLD"

def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)
    
    df['{}_target'.format(ticker)] = list(map( buy_sell_hold,
       df['{}_1d'.format(ticker)],
       df['{}_1d'.format(ticker)],
       df['{}_2d'.format(ticker)],
       df['{}_3d'.format(ticker)],
       df['{}_4d'.format(ticker)],
       df['{}_5d'.format(ticker)],
       df['{}_6d'.format(ticker)],
       df['{}_7d'.format(ticker)]))
    
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread:', Counter(str_vals))
    
    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)
    
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)
    
    X = df_vals.values
    y = df['{}_target'.format(ticker)].values
    
    return X, y, df

def do_ml(ticker):
    X, y, df = extract_featuresets(ticker)
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.25)
    
    # clf = KNeighborsClassifier()
    clf = VotingClassifier([('lsvc', LinearSVC(max_iter=10000)),
                            ('knn', KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])
    
    
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print('Accuracy', confidence)
    predictions = clf.predict(X_test)
    print('Predicted spread:', Counter(predictions))
    
    return confidence
    
print("IBM, Buy, Sell, Hold")
do_ml('IBM')
print("A, Buy, Sell, Hold")
do_ml('A')
print("AAPL, Buy, Sell, Hold")
do_ml('AAPL')
print("MMM, Buy, Sell, Hold")
do_ml('MMM')
print("ADP, Buy, Sell, Hold")
do_ml('ADP')
print("CBRE, Buy, Sell, Hold")
do_ml('CBRE')