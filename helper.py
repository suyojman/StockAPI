from config import API_KEY
import requests
import json
import csv
import time


def calculate_stock(symbol):
    response = requests.get(
        "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol="
        + symbol
        + "&apikey="
        + API_KEY
    )
    if response.status_code == 200:
        result = response.json()
        day = []
        a = 0
        for i in result["Time Series (Daily)"].keys():
            day.append(i)

    print("Preparing CSV for " + symbol + " ....")

    myData = ["Date", "Open", "High", "Low", "Close", "Volume"]
    with open("stock_info_" + symbol + ".csv", mode="w") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(myData)
        for j in day:
            writer.writerow(
                [
                    j,
                    result["Time Series (Daily)"][j]["1. open"],
                    result["Time Series (Daily)"][j]["2. high"],
                    result["Time Series (Daily)"][j]["3. low"],
                    result["Time Series (Daily)"][j]["4. close"],
                    result["Time Series (Daily)"][j]["5. volume"],
                ]
            )
    csvFile.close()
    time.sleep(2)
