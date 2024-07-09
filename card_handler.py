# card_handler.py
import datetime
import locale

from aiogram.utils.markdown import hbold, hlink
from pycbrf import ExchangeRates

from count_price import calculate_customs_fees, calculate_recycling_collection, calculate_customs_clearance, \
    calculate_excise_tax, calculate_vat
from predict_cars_auto_ru import compare_cars_encar_auto_ru
from translator import translator_translate


def create_card(brand, model, generation_encar_com, year_encar_com, fuel_type_encar_com, base_link_encar_com,
                formatted_mileage, formatted_price_won, encoded_data_encar_com, encoded_data_auto_ru, engine_power,
                engine_volume_cc):
    """
    Creates a car listing card with detailed information about the car, including pricing and similar cars in Russia.

    :param brand: The brand of the car.
    :param model: The model of the car.
    :param generation_encar_com: The generation of the car from encar.com.
    :param year_encar_com: The year of the car from encar.com.
    :param fuel_type_encar_com: The type of fuel the car uses from encar.com.
    :param base_link_encar_com: The base link for the car listing on encar.com.
    :param formatted_mileage: The formatted mileage of the car.
    :param formatted_price_won: The formatted price of the car in won.
    :param encoded_data_encar_com: Encoded data for the car from encar.com.
    :param encoded_data_auto_ru: Encoded data for similar cars from auto.ru.
    :param engine_power: The engine power of the car in horsepower.
    :param engine_volume_cc: The engine volume of the car in cubic centimeters.
    :return: A formatted string containing the car listing card.
    """
    # Translate fuel type to Russian.
    translated_fuel_type = translator_translate(fuel_type_encar_com)

    # Get today's date and exchange rates.
    today = str(datetime.datetime.now())[:10]
    rates_today = ExchangeRates(today)
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

    # Calculate customs fees, recycling collection, fee, excise tax, and VAT if engine details are available.
    if engine_power is None and engine_volume_cc is None:
        customs_fees = 0
        recycling_collection = 0
        fee = 0
        excise_tax = 0
        vat = 0
    else:
        customs_fees = calculate_customs_fees(int(year_encar_com), engine_volume_cc,
                                              int(formatted_price_won.replace(' ', '')), fuel_type_encar_com)
        recycling_collection = calculate_recycling_collection(int(year_encar_com), engine_volume_cc, fuel_type_encar_com)
        fee = calculate_customs_clearance(int(formatted_price_won.replace(' ', '')))
        excise_tax = calculate_excise_tax(engine_power, fuel_type_encar_com)
        vat = calculate_vat(int(formatted_price_won.replace(' ', '')), customs_fees, excise_tax, fuel_type_encar_com)

    # Calculate total price to Russia.
    price_to_Russia = round((int(formatted_price_won.replace(' ', '')) + 3100000) * float(rates_today['KRW'].rate) +
                            335000 + customs_fees + recycling_collection + fee + excise_tax + vat)
    formatted_price_to_Russia = locale.currency(price_to_Russia, grouping=True).split(',')[0]

    # Create message about similar cars in Russia.
    similar_cars_message = "Эта машина - эксклюзив! Таких в России нет."
    if engine_power is not None and engine_volume_cc is not None:
        if encoded_data_auto_ru is not None:
            similar_cars = compare_cars_encar_auto_ru(encoded_data_encar_com, encoded_data_auto_ru)
            if similar_cars:
                similar_cars_message = f"{hbold('Похожие объявления в России: ')}\n"
                for i, car in enumerate(similar_cars, 1):
                    similar_cars_message += f"{i}. {car}\n"

    # Create the car listing card.
    if engine_power is None and engine_volume_cc is None:
        card = (
            f"{hlink(f'{brand.upper()} {model.upper()} {generation_encar_com.upper()} {year_encar_com}', base_link_encar_com)}\n\n"
            f"{hbold('Пробег: ')} {formatted_mileage} км\n"
            f"{hbold('Год выпуска: ')} {year_encar_com}\n"
            f"{hbold('Тип топлива: ')} {translated_fuel_type.title()}\n\n"
            f"{hbold('Цена в вонах: ')} {formatted_price_won} ₩\n"
            f"{hbold('Цена привоза под ключ (без пошлин): ')} {formatted_price_to_Russia} ₽\n\n"
            f"Точную цену уточняйте у менеджера"
        )
    else:
        card = (
            f"{hlink(f'{brand.upper()} {model.upper()} {generation_encar_com.upper()} {year_encar_com}', base_link_encar_com)}\n\n"
            f"{hbold('Пробег: ')} {formatted_mileage} км\n"
            f"{hbold('Год выпуска: ')} {year_encar_com}\n"
            f"{hbold('Мощность двигателя: ')} {engine_power} л.с.\n"
            f"{hbold('Объем двигателя: ')} {round(engine_volume_cc / 1000, 1)} л\n"
            f"{hbold('Тип топлива: ')} {translated_fuel_type.title()}\n\n"
            f"{hbold('Цена в вонах: ')} {formatted_price_won} ₩\n"
            f"{hbold('Цена привоза под ключ: ')} {formatted_price_to_Russia} ₽\n\n"
            f"{similar_cars_message}"
        )

    return card
