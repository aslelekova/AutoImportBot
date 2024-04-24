import json
import math
import logging
import requests
import tqdm

from config import url_encar_com, headers_encar_com, url_auto_ru, headers_auto_ru
from file_handler import save_to_file

# Настройка логгера
logging.basicConfig(filename='parse_encar_com.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def parse_encar_com():
    logging.info('Starting Encar.com parsing')

    params = {"count": "true", "q": "(And.Hidden.N._.CarType.Y._.SellType.일반.)", "sr": "|ModifiedDate|20|20"}
    all_data = []

    response = requests.get(url_encar_com, params=params, headers=headers_encar_com)
    if response.status_code == 200:
        try:
            json_data = response.json()
            count = json_data.get("Count", 0)
            total_pages = math.ceil(count / 20)

            for page in tqdm.tqdm(range(total_pages)):
                params["sr"] = f"|ModifiedDate|{page * 20}|20"
                response = requests.get(url_encar_com, params=params, headers=headers_encar_com)
                if response.status_code == 200:
                    try:
                        json_data = response.json()
                        all_data.append(json_data)
                    except json.decoder.JSONDecodeError:
                        logging.error("Failed to parse JSON response")
                        break
                else:
                    logging.error(f"Failed to fetch data. Response code: {response.status_code}")
                    break

        except json.decoder.JSONDecodeError:
            logging.error("Failed to parse JSON response")
    else:
        logging.error(f"Failed to fetch data. Response code: {response.status_code}")

    logging.info('Encar.com parsing completed')
    return all_data




def parse_auto_ru():
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
        params = {"section": "all", "category": "cars", "geo_radius": 200, "geo_id": [213]}
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


parse_encar_com()
parse_auto_ru()

offers_data_auto_ru = parse_auto_ru()
offers_data_encar_com = parse_encar_com()
# Saving the parsed data to a file.
save_to_file(offers_data_auto_ru, "data_auto.json")
save_to_file(offers_data_encar_com, "data_encar.json")
