import sys
from pprint import pprint 
import requests

def run_stocks():
    symbol= input("Enter the market ticker: ")
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+ symbol + "&interval=1min&outputsize=compact&apikey=68H25FUXKAZOTV3O"
    try:
         res = requests.get(url)
         data = res.json()['Time Series (1min)']
         key = list(data.keys())[0]
         print("All figure as per 1 min charts.......\n\n")
         for k,v in data[key].items():
            print( k, v)
    except KeyError:
        print("Invalid ticker!")
        return

