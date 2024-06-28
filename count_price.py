# count_price.py
import datetime

from pycbrf import ExchangeRates


def calculate_customs_fees(year_encar_com, engine_volume, price_won, fuel_type):
    """
    Calculate the customs fees for a vehicle based on its age, engine volume, and price.

    The function determines the customs fee based on the vehicle's age, engine volume,
    and price in Korean Won. The conversion to Euro is done using the exchange rate from
    the Central Bank of Russia.

    :param fuel_type: The fuel type of the vehicle. Accepted values are 'ELECTRO' for electric vehicles and other
    types for non-electric vehicles.
    :param year_encar_com: The year of manufacture of the car.
    :param engine_volume: The engine volume of the vehicle in cubic centimeters.
    :param price_won: The price of the vehicle in Korean Won.
    :return: The calculated customs fee in Euro.
    """
    current_year = datetime.datetime.now().year
    today = str(datetime.datetime.now())[:10]
    rates_today = ExchangeRates(today)
    krw_to_rub_rate = float(rates_today['KRW'].rate)
    eut_to_rub_rate = float(rates_today['EUR'].rate)
    price_rub = price_won * krw_to_rub_rate
    price_eur = price_rub / eut_to_rub_rate
    if fuel_type != 'ELECTRO':
        if current_year - 3 <= year_encar_com <= current_year:
            if price_eur <= 8500:
                customs_fee = max(0.54 * price_won * krw_to_rub_rate, 2.5 * engine_volume * eut_to_rub_rate)
            elif 8500 < price_eur <= 16700:
                customs_fee = max(0.48 * price_won * krw_to_rub_rate, 3.5 * engine_volume * eut_to_rub_rate)
            elif 16700 < price_eur <= 42300:
                customs_fee = max(0.48 * price_won * krw_to_rub_rate, 5.5 * engine_volume * eut_to_rub_rate)
            elif 42300 < price_eur <= 84500:
                customs_fee = max(0.48 * price_won * krw_to_rub_rate, 7.5 * engine_volume * eut_to_rub_rate)
            elif 84500 < price_eur <= 169000:
                customs_fee = max(0.48 * price_won * krw_to_rub_rate, 15 * engine_volume * eut_to_rub_rate)
            else:
                customs_fee = max(0.48 * price_won * krw_to_rub_rate, 20 * engine_volume * eut_to_rub_rate)
        elif current_year - 5 <= year_encar_com < current_year - 3:
            if engine_volume <= 1000:
                customs_fee = 1.5 * engine_volume * eut_to_rub_rate
            elif 1000 < engine_volume <= 1500:
                customs_fee = 1.7 * engine_volume * eut_to_rub_rate
            elif 1500 < engine_volume <= 1800:
                customs_fee = 2.5 * engine_volume * eut_to_rub_rate
            elif 1800 < engine_volume <= 2300:
                customs_fee = 2.7 * engine_volume * eut_to_rub_rate
            elif 2300 < engine_volume <= 3000:
                customs_fee = 3.0 * engine_volume * eut_to_rub_rate
            else:
                customs_fee = 3.6 * engine_volume * eut_to_rub_rate
        elif year_encar_com < current_year - 5:
            if engine_volume <= 1000:
                customs_fee = 3.0 * engine_volume * eut_to_rub_rate
            elif 1000 < engine_volume <= 1500:
                customs_fee = 3.2 * engine_volume * eut_to_rub_rate
            elif 1500 < engine_volume <= 1800:
                customs_fee = 3.5 * engine_volume * eut_to_rub_rate
            elif 1800 < engine_volume <= 2300:
                customs_fee = 4.8 * engine_volume * eut_to_rub_rate
            elif 2300 < engine_volume <= 3000:
                customs_fee = 5.0 * engine_volume * eut_to_rub_rate
            else:
                customs_fee = 5.7 * engine_volume * eut_to_rub_rate
    else:
        customs_fee = 0.15 * price_won * krw_to_rub_rate
    return customs_fee


def calculate_recycling_collection(year_encar_com, engine_volume, fuel_type):
    """
    Calculates the recycling collection fee for a vehicle based on its engine capacity, fuel type, and age.

    :param year_encar_com: int
        The year of manufacture of the car.
    :param engine_volume: int
        The engine capacity of the vehicle in cubic centimeters (cc).
    :param fuel_type: str
        The fuel type of the vehicle. Accepted values are 'ELECTRO' for electric vehicles and other types for non-electric vehicles.

    :return: float
        The calculated recycling collection fee for the vehicle.
    """
    current_year = datetime.datetime.now().year
    if fuel_type != 'ELECTRO':
        if current_year - 3 <= year_encar_com <= current_year:
            if 0 <= engine_volume <= 3000:
                recycling_collection = 20000 * 0.17
            elif 3000 < engine_volume <= 3500:
                recycling_collection = 20000 * 48.5
            else:
                recycling_collection = 20000 * 61.76
        else:
            if 0 <= engine_volume <= 3000:
                recycling_collection = 20000 * 0.26
            elif 3000 < engine_volume <= 3500:
                recycling_collection = 20000 * 74.25
            else:
                recycling_collection = 20000 * 81.19
    else:
        if current_year - 3 <= year_encar_com <= current_year:
            recycling_collection = 20000 * 0.17
        else:
            recycling_collection = 20000 * 0.26
    return recycling_collection


def calculate_customs_clearance(price_won):
    """
   Calculate the customs clearance fee based on the price of the vehicle in euros.

   :param price_won: Price of the vehicle
   :return: Customs clearance fee in euros
   """
    today = str(datetime.datetime.now())[:10]
    rates_today = ExchangeRates(today)
    price_rub = float(rates_today['KRW'].rate) * price_won
    if price_rub <= 200000:
        fee = 775
    elif price_rub <= 450000:
        fee = 1550
    elif price_rub <= 1200000:
        fee = 3100
    elif price_rub <= 2700000:
        fee = 8530
    elif price_rub <= 4200000:
        fee = 12000
    elif price_rub <= 5500000:
        fee = 15500
    elif price_rub <= 7000000:
        fee = 20000
    elif price_rub <= 8000000:
        fee = 23000
    elif price_rub <= 9000000:
        fee = 25000
    elif price_rub <= 10000000:
        fee = 27000
    else:
        fee = 30000

    return fee


def calculate_excise_tax(engine_power_hp, fuel_type):
    """
    Calculate the excise tax for an electric vehicle based on engine power.

    :param fuel_type: The fuel type of the vehicle. Accepted values are 'ELECTRO' for electric vehicles and other
    types for non-electric vehicles.
    :param engine_power_hp: Engine power in horsepower (hp).
    :return: The excise tax in rubles.
    """
    if fuel_type == 'ELECTRO':
        if engine_power_hp <= 90:
            excise_tax = 0
        elif 90 < engine_power_hp <= 150:
            excise_tax = 58 * engine_power_hp
        elif 150 < engine_power_hp <= 200:
            excise_tax = 557 * engine_power_hp
        elif 200 < engine_power_hp <= 300:
            excise_tax = 912 * engine_power_hp
        elif 300 < engine_power_hp <= 400:
            excise_tax = 1555 * engine_power_hp
        elif 400 < engine_power_hp <= 500:
            excise_tax = 1609 * engine_power_hp
        else:
            excise_tax = 1662 * engine_power_hp
    else:
        excise_tax = 0
    return excise_tax


def calculate_vat(price_won, customs_fees, excise_tax, fuel_type):
    """
    Calculate the value-added tax (VAT) based on the total amount.

    :param price_won: The catalog price of the car.
    :param customs_fees: The customs duty.
    :param excise_tax: The excise tax.
    :param fuel_type: The fuel type of the vehicle. Accepted values are 'ELECTRO' for electric vehicles and other
    types for non-electric vehicles.
    :return: The calculated VAT amount.
    """
    today = str(datetime.datetime.now())[:10]
    rates_today = ExchangeRates(today)
    price_rub = float(rates_today['KRW'].rate) * price_won
    if fuel_type == 'ELECTRO':
        total_amount = price_rub + customs_fees + excise_tax
        vat = 0.20 * total_amount
    else:
        vat = 0
    return vat
