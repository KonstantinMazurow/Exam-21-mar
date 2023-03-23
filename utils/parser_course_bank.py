import requests
from data.config import BANK_API


def get_exchange_rate():
    response = requests.get(BANK_API).json()
    for i in list(response):
        if i['Cur_Abbreviation'] == 'USD':
            usd_exchange_rate = i['Cur_OfficialRate']
        if i['Cur_Abbreviation'] == 'EUR':
            eur_exchange_rate = i['Cur_OfficialRate']
        if i['Cur_Abbreviation'] == 'PLN':
            pln_exchange_rate = i['Cur_OfficialRate']
    return f"""Today cost of one BYN -
                            {usd_exchange_rate} USD,
                            {eur_exchange_rate} EUR,
                            {pln_exchange_rate} PLN"""
