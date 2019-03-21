import requests
import pprint
import json
import csv
import time
from config import API_KEY

a = input("Enter the symbol !! ")
symbol = a.upper()
how_many_days = input("Enter how many days from today !!")
response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey=' + API_KEY)


if response.status_code == 200:
    result = response.json()
    day = []
    a=0
    for i in result['Time Series (Daily)'].keys():
        a += 1
        if a > int(how_many_days):
            break
        day.append(i)
   
print("Preparing CSV....")


myData = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
with open('stock_info_'+symbol+ '.csv', mode='w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(myData)
    for j in day:
        writer.writerow([j, result["Time Series (Daily)"][j]["1. open"], result["Time Series (Daily)"][j]["2. high"], result["Time Series (Daily)"][j]["3. low"], result["Time Series (Daily)"][j]["4. close"], result["Time Series (Daily)"][j]["5. volume"]])
csvFile.close()
time.sleep(2)
print("DONE !!")