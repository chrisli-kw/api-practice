import os
import logging
import requests
from logging.handlers import RotatingFileHandler
from config import HOST, PORT


if not os.path.exists('./log'):
    os.makedirs('log')


logging.basicConfig(
    level='INFO',
    format='%(asctime)s.%(msecs)03d|%(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %a %H:%M:%S',
    handlers=[
            RotatingFileHandler(
                './log/unit_test.log', 'a', maxBytes=1*1024*1024, backupCount=2, encoding='utf-8'),
            logging.StreamHandler()
    ]
)


def get_data():
    return {
        "id": "A0000001",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district", "street": "fuxing-south-road"
        },
        "price": "1950",
        "currency": "TWD"
    }


def tester():
    url = f'http://{HOST}:{PORT}/api/orders'

    data = get_data()
    logging.info(f"Post to the API with accurate data")
    result = requests.post(url, json=data)
    logging.info('Test successfully')

    data = get_data()
    data['name'] = 'Melody Holiday Inn 123'
    logging.info(f"Test the API with name = {data['name']}:")
    result = requests.post(url, json=data)
    logging.info(result.text)

    data = get_data()
    data['name'] = 'melody holiday inn'
    logging.info(f"Test the API with name = {data['name']}:")
    result = requests.post(url, json=data)
    logging.info(result.text)

    data = get_data()
    data['price'] = '9999'
    logging.info(f"Test the API with price = {data['price']}:")
    result = requests.post(url, json=data)
    logging.info(result.text)

    data = get_data()
    data['currency'] = 'JPY'
    logging.info(f"Test the API with currency = {data['currency']}:")
    result = requests.post(url, json=data)
    logging.info(result.text)


if __name__ == "__main__":
    tester()
