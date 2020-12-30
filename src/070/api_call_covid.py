"""
Created 7-20-20 02:20 PM
Edited Last: 7-20-20 03:50 PM

@author: JS
"""

import requests


response = requests.get("https://coronavirusapi.com/getTimeSeries/PA")
if response:
    print("Request OK")
else:
    print("Request Failed")

