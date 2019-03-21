import requests
import pprint
import json

API_KEY = '904NLHZ1GSL4PIRX'
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
   

    for j in day:
        print("SYMBOL : " + result['Meta Data']['2. Symbol'])
        print("Date : " + j)
        print("OPEN : "+ result["Time Series (Daily)"][j]["1. open"])
        print("High : "+ result["Time Series (Daily)"][j]["2. high"])
        print("low : "+ result["Time Series (Daily)"][j]["3. low"])
        print("close : "+ result["Time Series (Daily)"][j]["4. close"])
        print("Volume : "+ result["Time Series (Daily)"][j]["5. volume"])
        print('***********************************')

    
