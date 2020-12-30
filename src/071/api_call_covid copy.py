"""
Created 7-20-20 02:20 PM
Edited Last: 7-20-20 03:50 PM

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


data = response.text


# the file to be converted to  
# json format 
#filename = 'data.txt'
  
# dictionary where the lines from 
# text will be stored 
dict1 = {} 
  
# creating dictionary 
with open(data) as fh: 
  
    for line in fh: 
  
        # reads each line and trims of extra the spaces  
        # and gives only the valid words 
        command, description = line.strip().split(None, 1) 
  
        dict1[command] = description.strip() 
  
# creating json file 
# the JSON file is named as test1 
# out_json = open("test1.json", "w") 
json.dump(dict1, indent = 4, sort_keys = False) 
out_json.close() 

parsed = json.loads(data)
print(json.dumps(parsed, indent=4))