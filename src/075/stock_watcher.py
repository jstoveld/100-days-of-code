"""
Created 7-29-20 5:00:00 PM
Edited Last: 7-29-20 5:00:00 PM

@author: JS
"""
#Imports our required modules
import requests


ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/tOIyE8ZwrY3YGk6xNBHvh'
requests.post(ifttt_webhook_url)

r = requests.post('https://finnhub.io/api/v1/webhook/add?token=bsq5530fkcbcavsjbj30', json={'event': 'earnings', 'symbol': 'AAPL'})
res = r.json()
print(res)

stock_api_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"

querystring = {"region":"US","lang":"en","symbol":"BA"}

# headers = {
#     'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
#     'x-rapidapi-key': "0d302faa6amsh4f64897b641b266p1ebe68jsn94822fcc3c88"
#     }

# response = requests.request("GET", stock_api_url, headers=headers, params=querystring)
# response_json = response.json()
# print(response_json)






# 
# type(response.json) #Our API will reply back with a list

# 




















# #User input to request stock prices
# stock = input("Please type in a stock ticker symbol to query:\n")

# #Definining our function parsePrice that will go and look for a specific element on the below URL
# #The input from the user is now converted into a literal sting with the 'f' at the start of the string. 
# #User can now query the stocks they want in real time.
# #Returning the current price
# def parsePrice():
#     r=requests.get(f'https://finance.yahoo.com/quote/{stock}')
#     soup=bs4.BeautifulSoup(r.text, "html.parser")
#     price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
#     return price


# def price_change(current, previous):
#     if (previous != 0):
#         return '%.10f'%(float(abs(current - previous) / previous) * 100.0)


# previous_price = 0
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S %p")
# print('The current price of 'f'({stock}) ''is: $'+str(parsePrice())+' at ' +current_time)


# #While loop that gathers this info until the function is interupted.
# #From the datetime.now we get the current time in h,m,s 
# #Name and value of the symbol as well as the timestamp are printed
# while True:
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S %p")
#     current_price = parsePrice()
#     if previous_price != current_price:
#         print('PRICE CHANGE! 'f'({stock}) '+str(price_change(current_price, previous_price))+'% '' is: $'+current_price+' at ' +current_time)
#         previous_price = current_price
#     time.sleep(70)