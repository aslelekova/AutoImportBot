# data_parser.py
import json
import logging
import math
import urllib.request as req
import requests
from config import url_auto_ru, headers_auto_ru, url_encar_com, headers_encar_com, cookies_encar_com

logger = logging.getLogger(__name__)


def parse_auto_ru(brand_auto_ru, model_auto_ru, year_left_bound, year_right_bound, fuel_type_auto_ru,
                  mileage_left_bound, mileage_right_bound):
    """
    Parse car data from auto.ru based on specified parameters.

    :param brand_auto_ru: The brand of the car on auto.ru.
    :param model_auto_ru: The model of the car on auto.ru.
    :param year_left_bound: The left bound of the year range.
    :param year_right_bound: The right bound of the year range.
    :param fuel_type_auto_ru: The fuel type of the car on auto.ru.
    :param mileage_left_bound: The left bound of the mileage range.
    :param mileage_right_bound: The right bound of the mileage range.
    :return: A list of car offers parsed from auto.ru.
    """
    offers = []
    page = 1
    # Loop until there are no more offers.
    while True:
        if year_left_bound == 0 and year_right_bound == 0: year_left_bound, year_right_bound = None, None
        if mileage_left_bound == 0 and mileage_right_bound == 0: mileage_left_bound, mileage_right_bound = None, None
        if fuel_type_auto_ru == '': fuel_type_auto_ru = None
        params = {
            "transmission": None,
            "engine_group": fuel_type_auto_ru,
            "year_from": year_left_bound,
            "year_to": year_right_bound,
            "section": "all",
            "km_age_from": mileage_left_bound,
            "km_age_to": mileage_right_bound,
            "category": "cars",
            "page": page,
            f"catalog_filter": [{"mark": brand_auto_ru, "model": model_auto_ru}],
            "geo_radius": 200,
            "geo_id": [213]
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
            logger.error(f"Error occurred while fetching data from auto.ru: {e}")
            break

    return offers


def parse_encar_com(brand_encar_com, model_encar_com, year_left_bound, year_right_bound, fuel_type_encar_com,
                    mileage_left_bound, mileage_right_bound):
    """
    Parse car data from encar.com based on specified parameters.

    :param brand_encar_com: The brand of the car on encar.com.
    :param model_encar_com: The model of the car on encar.com.
    :param year_left_bound: The left bound of the year range.
    :param year_right_bound: The right bound of the year range.
    :param fuel_type_encar_com: The fuel type of the car on encar.com.
    :param mileage_left_bound: The left bound of the mileage range.
    :param mileage_right_bound: The right bound of the mileage range.
    :return: A list of car data parsed from encar.com.
    """
    if mileage_right_bound == 0:
        mileage_right_bound = ''
    if mileage_left_bound == 0:
        mileage_left_bound = ''
    if year_left_bound == 0 and year_right_bound == 0:
        year_left_bound, year_right_bound = '0000', '9999'

    # Constructing parameters for the API request.
    if brand_encar_com in ["쉐보레(GM대우_)", "제네시스", "기아", "현대"]:
        if fuel_type_encar_com == "가솔린+전기 디젤+전기":
            params = {
                "count": "true",
                "q": f"(And.Year.range({str(year_left_bound)}00..{str(year_right_bound)}99)._.Mileage.range({str(mileage_left_bound)}..{str(mileage_right_bound)})._.Hidden.N._.SellType.일반._.("
                     f"Or.FuelType.가솔린+전기._.FuelType.디젤+전기.)_.(C.CarType.Y._.(C.Manufacturer.{brand_encar_com}._"
                     f".ModelGroup.{model_encar_com}.)))",
                "sr": "|ModifiedDate|0|20"
            }
        else:
            params = {
                "count": "true",
                "q": f"(And.Year.range({str(year_left_bound)}00..{str(year_right_bound)}99)._.Mileage.range({str(mileage_left_bound)}.."
                     f"{str(mileage_right_bound)})._.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.{brand_encar_com}._.ModelGroup."
                     f"{model_encar_com}.))_.SellType.일반._.FuelType.{fuel_type_encar_com}.)",
                "sr": "|ModifiedDate|0|20"
            }
    else:
        if fuel_type_encar_com == "가솔린+전기 디젤+전기":
            params = {
                "count": "true",
                "q": f"(And.Year.range({str(year_left_bound)}00..{str(year_right_bound)}99)._.Mileage.range({str(mileage_left_bound)}..{str(mileage_right_bound)})._.Hidden.N._.SellType.일반._.("
                     f"Or.FuelType.가솔린+전기._.FuelType.디젤+전기.)_.(C.CarType.N._.(C.Manufacturer.{brand_encar_com}._.ModelGroup.{model_encar_com}.)))",
                "sr": "|ModifiedDate|0|20"
            }
        else:
            params = {
                "count": "true",
                "q": f"(And.Year.range({str(year_left_bound)}00..{str(year_right_bound)}99)._.Mileage.range({str(mileage_left_bound)}.."
                     f"{str(mileage_right_bound)})._.Hidden.N._.(C.CarType.N._.(C.Manufacturer.{brand_encar_com}._.ModelGroup."
                     f"{model_encar_com}.))_.SellType.일반._.FuelType.{fuel_type_encar_com}.)",
                "sr": "|ModifiedDate|0|20"
            }

    all_data = []

    response = requests.get(url_encar_com, params=params, headers=headers_encar_com, cookies=cookies_encar_com)
    # Processing the API response.
    if response.status_code == 200:
        try:
            json_data = response.json()
            count = json_data.get("Count", 0)
            total_pages = math.ceil(count / 20)

            # Iterating over all pages of the API response.
            for page in range(total_pages):
                params["sr"] = f"|ModifiedDate|{page * 20}|20"
                response = requests.get(url_encar_com, params=params, headers=headers_encar_com,
                                        cookies=cookies_encar_com)
                # Parsing JSON data from each page.
                if response.status_code == 200:
                    try:
                        json_data = response.json()
                        all_data.append(json_data)
                    except json.decoder.JSONDecodeError:
                        logger.error("Error: Unable to parse response to JSON")
                        break
                else:
                    logger.error(f"Error: Failed to make request. Response code: {response.status_code}")
                    break

        except json.decoder.JSONDecodeError:
            logger.error("Error: Unable to parse response to JSON")
    else:
        logger.error(f"Error: Failed to make request. Response code: {response.status_code}")
    return all_data
