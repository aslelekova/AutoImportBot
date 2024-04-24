# data_parser.py
import json
import math
from config import url_auto_ru, headers_auto_ru, url_encar_com, headers_encar_com
import requests


def parse_auto_ru(brand_auto_ru, model_auto_ru, year_left_bound, year_right_bound, fuel_type_auto_ru):
    offers = []
    page = 1
    # Loop until there are no more offers.
    while True:
        # ToDo: get params from bot.
        # params = {
        #     "displacement_from": None,
        #     "displacement_to": None,
        #     "transmission": None,
        #     "gear_type": None,
        #     "engine_group": fuel_type_auto_ru,
        #     "year_from": int(year_left_bound),
        #     "year_to": int(year_right_bound),
        #     "price_from": None,
        #     "price_to": 6000000,
        #     "section": "all",
        #     "km_age_from": None,
        #     "km_age_to": 100000,
        #     "category": "cars",
        #     "page": page,
        #     f"catalog_filter": [{"mark": brand_auto_ru, "model": model_auto_ru}],
        #     "geo_radius": 200,
        #     "geo_id": [213]
        # }
        {"section": "all", "category": "cars", "geo_radius": 200, "geo_id": [213]}
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
    params = {"count": "true", "q": "(And.Hidden.N._.CarType.Y.)", "sr": "|ModifiedDate|20|20"}

    all_data = []

    response = requests.get(url_encar_com, params=params, headers=headers_encar_com)
    if response.status_code == 200:
        try:
            json_data = response.json()
            count = json_data.get("Count", 0)
            total_pages = math.ceil(count / 20)

            for page in range(total_pages):
                params["sr"] = f"|ModifiedDate|{page * 20}|20"
                response = requests.get(url_encar_com, params=params, headers=headers_encar_com)
                if response.status_code == 200:
                    try:
                        json_data = response.json()
                        all_data.append(json_data)
                    except json.decoder.JSONDecodeError:
                        print("Ошибка: Невозможно преобразовать ответ в JSON")
                        break
                else:
                    print(f"Ошибка: Не удалось выполнить запрос. Код ответа: {response.status_code}")
                    break

        except json.decoder.JSONDecodeError:
            print("Ошибка: Невозможно преобразовать ответ в JSON")
    else:
        print(f"Ошибка: Не удалось выполнить запрос. Код ответа: {response.status_code}")
    return all_data
