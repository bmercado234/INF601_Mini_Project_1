# INF601 - Advanced Programming in Python
# Braulio Mercado
# Mini Project 1
#https://rapidapi.com/asepscareer/api/yfinance-stock-market-data/

import requests
from config import *
import pprint


url = "https://yfinance-stock-market-data.p.rapidapi.com/price-customdate"

#aapl, msft, googl, meta, tsla
payload = {
	"symbol": "tsla",
	"end": "2023-09-09",
	"start": "2023-08-25"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": X_RapidAPI_Key,
	"X-RapidAPI-Host": "yfinance-stock-market-data.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

pprint.pprint(response.json())
