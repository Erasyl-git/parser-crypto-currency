import requests
from Cryptocurrency.models import CryptoCurrency
from datetime import datetime


def get_info():
    response = requests.get(url='https://api.bybit.com/v2/public/tickers')
    data = response.json()
    cryptocurrency = data['result']

    for crypto_data in cryptocurrency:
        CryptoCurrency.objects.create(
            name=crypto_data['symbol'],
            currency = 'USD',
            price=crypto_data['last_price'],
            volume=crypto_data['volume_24h'],
            change=crypto_data['price_24h_pcnt'],
            last_updated=datetime.now()
        )
