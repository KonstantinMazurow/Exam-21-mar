import requests
from data.config import CRYPTO_API


def get_info_btc():
    r = requests.get(CRYPTO_API)
    data = r.json()
    btc = data[0]["quotes"]["USD"]["price"]
    return btc
