import bs4 
import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate


dfs = pd.read_html('https://www.hockey-reference.com/leagues/NHL_2020_leaders.html')
for df in dfs:
    print(tabulate(df, headers='keys', tablefmt='psql'))