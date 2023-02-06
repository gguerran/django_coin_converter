import requests


def convert_service(from_currency, to_currency, amount):
    response = requests.get(
        f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    ).json()
    return {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted": response["result"],
        "date": response["date"],
    }
