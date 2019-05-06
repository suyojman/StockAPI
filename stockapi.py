import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader as web
from helper import calculate_stock

input_symbols = input("Enter one or more symbol seperated by a comma ")
splitted_symbols = input_symbols.split(",")
print(splitted_symbols)

symbols = [a.upper() for a in splitted_symbols]
for symbol in symbols:
    calculate_stock(symbol)


print("Finishing!!")

# Plotting the graph

# style.use("ggplot")
# start = dt.datetime(2002,1,1)
# end = dt.datetime.now()
# print(end)
# df = web.get_data_yahoo(symbol, start, end)
# df["Adj Close"].plot()
# plt.show()

# print("DONE !!")
