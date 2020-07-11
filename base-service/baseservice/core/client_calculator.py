import os
import requests

CALCULATOR_URL = os.environ.get('CALCULATOR_URL', "http://localhost:3333")


def get_discount(product_id, user_id):
    filter_user = f"?userId={user_id}" if user_id else ""
    url = f"{CALCULATOR_URL}/discounts/{product_id}/{filter_user}"
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.ConnectionError as error:
        raise ConnectionError
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            return None

        raise error

    return r.json()


if __name__ == "__main__":
    try:
        discount = get_discount(1, 1)
        print(discount)
    except Exception as error:
        if isinstance(error, ConnectionError):
            print("Connection Refused")
        else:
            print(error)
