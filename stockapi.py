import requests
import pprint
import json
import csv
import time
import datetime as dt
from config import API_KEY
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader as web


a = input("Enter the symbol !! ")
symbol = a.upper()
response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol='+symbol+'&apikey=' + API_KEY)


if response.status_code == 200:
    result = response.json()
    day = []
    a=0
    for i in result['Time Series (Daily)'].keys():
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

print("Preparing Graph!!")

#Plotting the graph

style.use("ggplot")
start = dt.datetime(2002,1,1)
end = dt.datetime.now()
print(end)
df = web.get_data_yahoo(symbol, start, end)
df["Adj Close"].plot()
plt.show()

print("DONE !!")