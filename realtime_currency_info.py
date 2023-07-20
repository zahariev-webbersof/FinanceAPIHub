import requests

# API key is obtained from Alpha Vantage website: https://www.alphavantage.co/
# After visiting the website, click on 'Get your free API key' button
# Fill out the form, and your API key will be generated
API_KEY = 'CKQIZXHUPEU9PKQS'
FROM_CURRENCY = 'USD'
TO_CURRENCY = 'EUR'
base_url = 'https://www.alphavantage.co/query?'

params = {
    "function": "CURRENCY_EXCHANGE_RATE",
    "from_currency": FROM_CURRENCY,
    "to_currency": TO_CURRENCY,
    "apikey": API_KEY
}

response = requests.get(base_url, params=params)
data = response.json()

print('Realtime Currency Exchange Rate Data:')
print('From Currency:', FROM_CURRENCY)
print('To Currency:', TO_CURRENCY)

# Retrieve current exchange rate from the response data
current_rate_usd_eur = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
print('Current Rate USD-EUR:', current_rate_usd_eur)

# Assuming the bid price, ask price and last refreshed are part of the 'Realtime Currency Exchange Rate' in the response data
# Retrieve bid price from the response data
bid_price = data['Realtime Currency Exchange Rate']['8. Bid Price']
print('Bid Price:', bid_price)

# Retrieve ask price from the response data
ask_price = data['Realtime Currency Exchange Rate']['9. Ask Price']
print('Ask Price:', ask_price)

# Retrieve last refreshed time from the response data
last_refreshed = data['Realtime Currency Exchange Rate']['6. Last Refreshed']
print('Last Refreshed:', last_refreshed)

"""
Example output:
Realtime Currency Exchange Rate Data:
From Currency: USD
To Currency: EUR
Current Rate USD-EUR: 0.89592000
Bid Price: 0.89587700
Ask Price: 0.89594400
Last Refreshed: 2023-07-20 14:26:03
"""