"""
Created 7-20-20 02:20 PM
Edited Last: 7-24-20 01:50 PM

@author: JS
"""

import json
import requests
import pandas as pd
import matplotlib


#Defines our URL we are targeting to get our data
url = "https://api.covid19api.com/summary"

#Lets us know if this is OK or will fail
response = requests.get(url)
if response:
    print("Request OK")
else:
    print("Request Failed")


data = response.json()
print(json.dumps(data, indent=4))