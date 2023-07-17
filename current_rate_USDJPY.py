import requests

def get_price_eur_jpy():
    url = 'https://www.freeforexapi.com/api/live?pairs=USDJPY'

    try:
        response = requests.get(url)
        date = response.json()
        rate = date['rates']['USDJPY']['rate']
        return rate

    except requests.exceptions.RequestException as e:
        print('Error:', e)

current_rate_EURJPY = get_price_eur_jpy()

print(current_rate_EURJPY)