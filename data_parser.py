# data_parser.py
from config import url, headers
import requests


def parse_auto_ru():
    offers = []
    page = 1
    # Loop until there are no more offers.
    while True:
        # ToDo: get params from bot.
        params = {
            "year_from": 2022,
            "year_to": 2023,
            "section": "all",
            "category": "cars",
            "page": page,
            "catalog_filter": [{"mark": "GEELY", "model": "ATLAS"}],
            "geo_id": []
        }

        try:
            # Make a POST request with parameters and headers.
            response = requests.post(url, json=params, headers=headers)

            # Parse the JSON response.
            data = response.json()

            # Extract new offers from the response.
            new_offers = data.get('offers', [])

            if not new_offers:
                break

            offers.extend(new_offers)
            page += 1

        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching data: {e}")
            break

    return offers


def parse_encar_com():
    pass