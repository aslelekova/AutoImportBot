# car_analysis.py
import locale

from aiogram.utils.markdown import hbold, hlink
from googletrans import Translator

from count_price import get_rates
from predict_cars_auto_ru import encode_fuel_type, compare_cars_encar_auto_ru


def analyze_car_data_auto_ru(data_auto_ru):
    """
    Analyze the data obtained from auto.ru to extract relevant information about cars.

    :param data_auto_ru: The data obtained from auto.ru.
    :return: The brand, model, and encoded data about cars.
    """
    if not data_auto_ru:
        return None
    vectors_auto_ru = {}
    for item in data_auto_ru:
        vector_auto_ru = []
        # Extracting brand, model, and price information from the data.
        brand = item.get("vehicle_info", {}).get("mark_info", {}).get("code", "").lower()
        model = item.get("vehicle_info", {}).get("model_info", {}).get("code", "").lower()
        generation_auto_ru = item.get("vehicle_info", {}).get("super_gen", {}).get("name", "").lower()
        year_auto_ru = item.get("documents", {}).get("year", {})
        price_rub = item.get("price_info", {}).get("price", "")
        mileage = item.get("state", {}).get("mileage", "")
        fuel_type = item.get("vehicle_info", {}).get("tech_param", {}).get("engine_type", "")

        # Getting information about whether the car is new or used.
        is_used = item.get("section") == "used"
        complectation_id = item.get("vehicle_info", {}).get("complectation", {}).get("id", "")
        tech_param_id = item.get("vehicle_info", {}).get("tech_param", {}).get("id", "")
        sale_id = item.get("saleId", "")

        base_link_auto_ru = create_link_auto_ru(brand, model, sale_id, tech_param_id, complectation_id, is_used,
                                                generation_auto_ru, year_auto_ru)

        vector_auto_ru.append(price_rub)
        vector_auto_ru.append(mileage)
        vector_auto_ru.append(fuel_type)
        vector_auto_ru.append(year_auto_ru)
        vectors_auto_ru[base_link_auto_ru] = vector_auto_ru
    encoded_data_auto_ru = encode_fuel_type(vectors_auto_ru)

    return brand, model, encoded_data_auto_ru


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
    translated_generation = translator_translate(generation_encar_com)
    mileage = item.get("Mileage", "")
    formatted_mileage = '{:,.0f}'.format(mileage).replace(',', ' ')

    # Format price and year information.
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    formatted_price_won = '{:,.0f}'.format(price_won * 10000).replace(',', ' ')
    year_encar_com = str(item.get("Year", ""))[:4]
    fuel_type_encar_com = item.get("FuelType", "")
    base_link_encar_com = f"http://www.encar.com/dc/dc_cardetailview.do?carid={id}"

    # ToDo: change price_won on price with taxes
    # Calculate car vector components.
    vector_encar_com.append(price_won * 10000 * get_rates()['KRW'][1])
    vector_encar_com.append(mileage)

    # Map Korean fuel types to English.
    if fuel_type_encar_com == '가솔린': fuel_type_encar_com = 'GASOLINE'
    if fuel_type_encar_com == '디젤': fuel_type_encar_com = 'DIESEL'
    if fuel_type_encar_com == '전기': fuel_type_encar_com = 'ELECTRO'
    if fuel_type_encar_com == '가솔린+전기' or fuel_type_encar_com == '디젤+전기': fuel_type_encar_com = 'HYBRID'

    vector_encar_com.append(fuel_type_encar_com)
    vector_encar_com.append(year_encar_com)

    # Encode fuel type and create car card.
    encoded_data_encar_com = encode_fuel_type({base_link_encar_com: vector_encar_com})
    return create_card(brand, model, translated_generation, year_encar_com, fuel_type_encar_com,
                       base_link_encar_com, formatted_mileage, formatted_price_won,
                       encoded_data_encar_com, encoded_data_auto_ru)


def create_link_auto_ru(brand, model, sale_id, tech_param_id, complectation_id, is_used, generation_auto_ru,
                        year_auto_ru):
    # Formatting the base part of the link.
    base_link = f"https://auto.ru/cars/"

    # Adding type of the car (new or used) to the link.
    if is_used:
        base_link += f"used/sale/{brand.lower()}/{model.lower()}/{sale_id}/"
    else:
        base_link += f"new/group/{brand.lower()}/{model.lower()}/{tech_param_id}/{complectation_id}/{sale_id}"

    link = hlink(f'{brand.upper()} {model.title()} {generation_auto_ru.upper()} {year_auto_ru}', base_link)
    return link


translator = Translator()


def translator_translate(word):
    result = translator.translate(word, dest='en')
    return result.text


def create_card(brand, model, generation_encar_com, year_encar_com, fuel_type_encar_com, base_link_encar_com,
                formatted_mileage, formatted_price_won, encoded_data_encar_com, encoded_data_auto_ru):
    translated_fuel_type = translator_translate(fuel_type_encar_com)
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    price_to_Russia = round((int(formatted_price_won.replace(' ', '')) + 3100000) * get_rates()['KRW'][1] + 335000)
    formatted_price_to_Russia = locale.currency(price_to_Russia, grouping=True).split(',')[0]
    if not encoded_data_auto_ru:
        similar_cars_message = "Эта машина - эксклюзив!"
    else:
        similar_cars = compare_cars_encar_auto_ru(encoded_data_encar_com, encoded_data_auto_ru)
        similar_cars_message = f"{hbold('Похожие объявления в России: ')}\n"
        array_length = len(similar_cars)
        for i in range(min(array_length, 3)):
            similar_cars_message += f"{i + 1}. {similar_cars[i]}\n"

    card = (
        f"{hlink(f'{brand.upper()} {model.upper()} {generation_encar_com.upper()} {year_encar_com}', base_link_encar_com)}\n\n"
        f"{hbold('Пробег: ')} {formatted_mileage} км\n"
        f"{hbold('Год выпуска: ')} {year_encar_com}\n"
        f"{hbold('Тип топлива: ')} {translated_fuel_type.title()}\n\n"
        f"{hbold('Цена в вонах: ')} {formatted_price_won} ₩\n"
        f"{hbold('Цена привоза под ключ: ')} {formatted_price_to_Russia} ₽\n\n"
        f"{similar_cars_message}"
    )

    return card
