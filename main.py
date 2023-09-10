# INF601 - Advanced Programming in Python
# Braulio Mercado
# Mini Project 1
#https://rapidapi.com/asepscareer/api/yfinance-stock-market-data/

import requests
from config import *
import pprint
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import shutil, os
from pathlib import Path

if not os.path.exists('charts'):
	os.makedirs('charts')



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
aapl_arr = np.array(aapl_close_price)

#msft [322.9800109863, 323.700012207, 328.4100036621, 328.7900085449, 327.7600097656, 328.6600036621, 333.549987793, 332.8800048828, 329.9100036621, 334.2699890137]
msft_close_price = [322.9800109863, 323.700012207, 328.4100036621, 328.7900085449, 327.7600097656,
328.6600036621, 333.549987793, 332.8800048828, 329.9100036621, 334.2699890137]
msft_arr = np.array(msft_close_price)

#googl [129.8800048828, 131.0099945068, 134.5700073242, 135.8800048828, 136.1699981689, 135.6600036621, 135.7700042725, 134.4600067139, 135.2599945068, 136.3800048828]
googl_close_price = [129.8800048828, 131.0099945068, 134.5700073242, 135.8800048828, 136.1699981689,
 135.6600036621, 135.7700042725, 134.4600067139, 135.2599945068, 136.3800048828]
googl_arr = np.array(googl_close_price)

#meta [285.5, 290.2600097656, 297.9899902344, 295.1000061035, 295.8900146484, 296.3800048828, 300.1499938965, 299.1700134277, 298.6700134277, 297.8900146484]
meta_close_price = [285.5, 290.2600097656, 297.9899902344, 295.1000061035, 295.8900146484,
 296.3800048828, 300.1499938965, 299.1700134277, 298.6700134277, 297.8900146484]
meta_arr = np.array(meta_close_price)

#tsla [238.5899963379, 238.8200073242, 257.1799926758, 256.8999938965, 258.0799865723, 245.0099945068, 256.4899902344, 251.9199981689, 251.4900054932, 248.5]
tsla_close_price = [238.5899963379, 238.8200073242, 257.1799926758, 256.8999938965, 258.0799865723,
 245.0099945068, 256.4899902344, 251.9199981689, 251.4900054932, 248.5]
tsla_arr = np.array(tsla_close_price)


fig, aapl_ax = plt.subplots()
aapl_ax.set_ylabel('Closing Price')
aapl_ax.set_title('Apple (AAPL) Closing Price Last 10 Trading Days (2023/08/25 - 2023/09/09)')
aapl_ax.grid(True)
aapl_ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], aapl_arr)
plt.savefig('aapl_fig')
shutil.move('aapl_fig.png', 'charts')

fig, msft_ax = plt.subplots()
msft_ax.set_ylabel('Closing Price')
msft_ax.set_title('Microsoft (MSFT) Closing Price Last 10 Trading Days (2023/08/25 - 2023/09/09)')
msft_ax.grid(True)
msft_ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], msft_arr)
plt.savefig('msft_fig')
shutil.move('msft_fig.png', 'charts')

fig, googl_ax = plt.subplots()
googl_ax.set_ylabel('Closing Price')
googl_ax.set_title('Alphabet (GOOGL) Closing Price Last 10 Trading Days (2023/08/25 - 2023/09/09)')
googl_ax.grid(True)
googl_ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], googl_arr)
plt.savefig('googl_fig')
shutil.move('googl_fig.png', 'charts')

fig, meta_ax = plt.subplots()
meta_ax.set_ylabel('Closing Price')
meta_ax.set_title('Meta (META) Closing Price Last 10 Trading Days (2023/08/25 - 2023/09/09)')
meta_ax.grid(True)
meta_ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], meta_arr)
plt.savefig('meta_fig')
shutil.move('meta_fig.png', 'charts')

fig, tsla_ax = plt.subplots()
tsla_ax.set_ylabel('Closing Price')
tsla_ax.set_title('Tesla (TSLA) Closing Price Last 10 Trading Days (2023/08/25 - 2023/09/09)')
tsla_ax.grid(True)
tsla_ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], tsla_arr)
plt.savefig('tsla_fig')
shutil.move('tsla_fig.png', 'charts')