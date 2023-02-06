import requests
from datetime import datetime


def convert_service(from_currency, to_currency, amount):

    response = requests.get(
        f"https://min-api.cryptocompare.com/data/price?fsym={from_currency}&tsyms={to_currency}"
    ).json()
    return {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted": amount * response[to_currency],
        "date": datetime.now().date(),
    }
