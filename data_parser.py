# data_parser.py
import file_handler
from config import url_auto_ru, headers_auto_ru, url_encar_com, headers_encar_com
import requests


def parse_auto_ru():

    offers = []
    page = 1
    # Loop until there are no more offers.
    while True:
        # ToDo: get params from bot.
        params = {
            "displacement_from": 200,
            "displacement_to": 5500,
            "transmission": "AUTOMATIC",
            "gear_type": "ALL_WHEEL_DRIVE",
            "engine_group": "GASOLINE",
            "year_from": 2019,
            "year_to": 2024,
            "price_from": None,
            "price_to": 8000000,
            "section": "all",
            "km_age_from": None,
            "km_age_to": 100000,
            "category": "cars",
            "page": page,
            "catalog_filter": [{"mark": "BMW", "model": "M5"}],
            "geo_id": []
        }

        try:
            # Make a POST request with parameters and headers.
            response = requests.post(url_auto_ru, json=params, headers=headers_auto_ru)

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
    params = {
                 "count": "true",
                 "q": "(And.Year.range(201500..202199)._.Mileage.range(20000..120000)._.Hidden.N._.(C.CarType.N._.(C.Manufacturer.랜드로버._.ModelGroup.디스커버리.))_.FuelType.디젤.)",
                 "sr": "|ModifiedDate|0|8"
    }
    response = requests.post(url_encar_com, json=params, headers=headers_encar_com)
    data = response.json()
    file_handler.save_to_file(data, "encar.json")
