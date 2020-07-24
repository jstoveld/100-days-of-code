"""
Created 7-20-20 02:20 PM
Edited Last: 7-24-20 03:50 PM

@author: JS
"""

import json
import requests
from requests.models import Response


#Defines our URL we are targeting to get our data
url = "https://coronavirusapi.com/getTimeSeries/PA"
#test url = "https://api.exchangeratesapi.io/latest?symbols=USD,GBP"

#Lets us know if this is OK or will fail
response = requests.get(url)
if response:
    print("Request OK")
else:
    print("Request Failed")


data = response.json

parsed = json.loads(data)
print(json.data(parsed, indent=4))