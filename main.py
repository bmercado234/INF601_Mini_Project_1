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

data = response.json()

adj_close_values = [item['Adj Close'] for item in data['data']]

print(adj_close_values)

#aapl [178.6100006104, 180.1900024414, 184.1199951172, 187.6499938965, 187.8699951172, 189.4600067139, 189.6999969482, 182.9100036621, 177.5599975586, 178.1799926758]
aapl_close_price = [178.6100006104, 180.1900024414, 184.1199951172, 187.6499938965, 187.8699951172,
189.4600067139, 189.6999969482, 182.9100036621, 177.5599975586, 178.1799926758]

