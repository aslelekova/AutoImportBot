# car_analysis.py
import locale
import logging

import translator
from aiogram.utils.markdown import hlink

from card_handler import create_card
from file_handler import load_data_from_json
from predict_cars_auto_ru import encode_fuel_type

logging.basicConfig(filename='bot.log', level=logging.INFO)
logger = logging.getLogger(__name__)


def analyze_car_data_auto_ru(data_auto_ru):
    """
    Analyze the data obtained from auto.ru to extract relevant information about cars.

    :param data_auto_ru: The data obtained from auto.ru.
    :return: The encoded data about cars.
    """
    if not data_auto_ru:
        return None
    vectors_auto_ru = {}
    for item in data_auto_ru:
        vector_auto_ru = []

        # Extracting brand, model, and price information from the data.
        brand_auto_ru = item.get("vehicle_info", {}).get("mark_info", {}).get("code", "").lower()
        model_auto_ru = item.get("vehicle_info", {}).get("model_info", {}).get("code", "").lower()
        generation_auto_ru = item.get("vehicle_info", {}).get("super_gen", {}).get("name", "").lower()
        year_auto_ru = item.get("documents", {}).get("year", {})
        mileage = item.get("state", {}).get("mileage", "")
        fuel_type = item.get("vehicle_info", {}).get("tech_param", {}).get("engine_type", "")

        engine_power = item.get("vehicle_info", {}).get("tech_param", {}).get("power", "")
        engine_volume = item.get("vehicle_info", {}).get("tech_param", {}).get("displacement", "")

        # Getting information about whether the car is new or used.
        is_used = item.get("section") == "used"
        complectation_id = item.get("vehicle_info", {}).get("complectation", {}).get("id", "")
        tech_param_id = item.get("vehicle_info", {}).get("tech_param", {}).get("id", "")
        sale_id = item.get("saleId", "")

        base_link_auto_ru = create_link_auto_ru(brand_auto_ru, model_auto_ru, sale_id, tech_param_id, complectation_id,
                                                is_used, generation_auto_ru, year_auto_ru)

        vector_auto_ru.append(engine_power)
        vector_auto_ru.append(engine_volume)
        vector_auto_ru.append(mileage)
        vector_auto_ru.append(fuel_type)
        vector_auto_ru.append(year_auto_ru)
        vectors_auto_ru[base_link_auto_ru] = vector_auto_ru

    encoded_data_auto_ru = encode_fuel_type(vectors_auto_ru)

    return encoded_data_auto_ru


def process_item_encar_com(item, brand, model, encoded_data_auto_ru):
    """
    Process an item obtained from encar.com to extract relevant information about cars.

    :param item: The item obtained from encar.com.
    :param brand: The brand of the car.
    :param model: The model of the car.
    :param encoded_data_auto_ru: Encoded data about cars obtained from auto.ru.
    :return: A card containing information about the car.
    """
    vector_encar_com = []

    # Check if the car is a duplicate or not.
    service_copy_car = item.get("ServiceCopyCar", "")
    if service_copy_car == "DUPLICATION":
        return None

    # Check if the price is valid.
    price_won = item.get("Price", "")
    if price_won == 0 or price_won == 9999.0 or price_won == 99999.0:
        return None

    # Extract relevant car information.
    id = item.get("Id", "")
    generation_encar_com = item.get("Badge", "")
    translated_generation = translator.translator_translate(generation_encar_com)
    mileage = item.get("Mileage", "")
    formatted_mileage = '{:,.0f}'.format(mileage).replace(',', ' ')

    # Format price and year information.
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    formatted_price_won = '{:,.0f}'.format(price_won * 10000).replace(',', ' ')
    year_encar_com = str(item.get("Year", ""))[:4]
    fuel_type_encar_com = item.get("FuelType", "")
    base_link_encar_com = f"http://www.encar.com/dc/dc_cardetailview.do?carid={id}"

    if fuel_type_encar_com == "수소" or fuel_type_encar_com == "LPG(일반인 구입)":
        return None

    engines_data = load_data_from_json("engines.json")
    engine_power = engines_data.get(brand, {}).get(model, {}).get(generation_encar_com, {}).get('engine_power')
    engine_volume_cc = engines_data.get(brand, {}).get(model, {}).get(generation_encar_com, {}).get('engine_volume_cc')

    # Calculate car vector components.
    vector_encar_com.append(engine_power)
    vector_encar_com.append(engine_volume_cc)
    vector_encar_com.append(mileage)

    # Map Korean fuel types to English.
    if fuel_type_encar_com == '가솔린':
        fuel_type_encar_com = 'GASOLINE'
    if fuel_type_encar_com == '디젤':
        fuel_type_encar_com = 'DIESEL'
    if fuel_type_encar_com == '전기':
        fuel_type_encar_com = 'ELECTRO'
    if fuel_type_encar_com == '가솔린+전기' or fuel_type_encar_com == '디젤+전기':
        fuel_type_encar_com = 'HYBRID'

    vector_encar_com.append(fuel_type_encar_com)
    vector_encar_com.append(year_encar_com)

    # Encode fuel type and create car card.
    encoded_data_encar_com = encode_fuel_type({base_link_encar_com: vector_encar_com})

    return create_card(brand, model, translated_generation, year_encar_com, fuel_type_encar_com,
                       base_link_encar_com, formatted_mileage, formatted_price_won,
                       encoded_data_encar_com, encoded_data_auto_ru, engine_power, engine_volume_cc)


def create_link_auto_ru(brand_auto_ru, model_auto_ru, sale_id, tech_param_id, complectation_id, is_used,
                        generation_auto_ru, year_auto_ru):
    """
    Creates a hyperlink for a car listing on auto.ru based on provided parameters.

    :param brand_auto_ru: The brand of the car on auto.ru.
    :param model_auto_ru: The model of the car on auto.ru.
    :param sale_id: The unique sale identifier for the car listing.
    :param tech_param_id: The technical parameter identifier for the car listing.
    :param complectation_id: The complectation identifier for the car listing.
    :param is_used: Boolean indicating if the car is used (True) or new (False).
    :param generation_auto_ru: The generation of the car on auto.ru.
    :param year_auto_ru: The year of the car on auto.ru.
    :return: A formatted hyperlink string for the car listing.
    """

    # Formatting the base part of the link.
    base_link = f"https://auto.ru/cars/"

    # Adding type of the car (new or used) to the link.
    if is_used:
        base_link += f"used/sale/{brand_auto_ru.lower()}/{model_auto_ru.lower()}/{sale_id}/"
    else:
        base_link += (f"new/group/{brand_auto_ru.lower()}/{model_auto_ru.lower()}/{tech_param_id}/{complectation_id}/"
                      f"{sale_id}")

    link = hlink(f'{brand_auto_ru.upper()} {model_auto_ru.upper()} {generation_auto_ru.upper()} {year_auto_ru}',
                 base_link)

    return link
