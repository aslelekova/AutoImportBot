# count_price.py
import datetime

from pycbrf import ExchangeRates


def get_rates():
    """
    Function to retrieve exchange rates for specified currencies.

    :return: A dictionary containing exchange rates for the specified currencies.
             The keys represent currency codes, and the values are lists containing:
             - Currency name
             - Exchange rate to the base currency (float)
             - Value of the currency in the base currency (float)
    """
    rates = {}
    to_show_rates = ['KRW', 'RUB']
    today = str(datetime.datetime.now())[:10]
    rates_today = ExchangeRates(today)
    for rate in list(filter(lambda el: el.code in to_show_rates, rates_today.rates)):
        rates[rate.code] = [rate.name, float(rate.rate), float(rate.value)]
    return rates


# def get_customs_fees(year_left_bound, year_right_bound, engine_capacity, engine_power, price_won, fluent_type):
#     current_year = datetime.now().year
#     if year_left_bound >= current_year - 3 and year_right_bound <= current_year:
#         pass
#     elif year_left_bound >= (current_year - 5) and year_right_bound < (current_year - 3):
#         pass


def get_recycling_collection(year_left_bound, year_right_bound, engine_capacity, fuel_type):
    """
    Calculates the recycling collection fee for a vehicle based on its engine capacity, fuel type, and age.

    :param year_left_bound: int
        The lower bound of the vehicle's production year range.
    :param year_right_bound: int
        The upper bound of the vehicle's production year range.
    :param engine_capacity: int
        The engine capacity of the vehicle in cubic centimeters (cc).
    :param fuel_type: str
        The fuel type of the vehicle. Accepted values are 'ELECTRO' for electric vehicles and other types for non-electric vehicles.

    :return: float
        The calculated recycling collection fee for the vehicle.
    """
    current_year = datetime.now().year
    if fuel_type != 'ELECTRO':
        if year_left_bound >= current_year - 3 and year_right_bound <= current_year:
            if 0 <= engine_capacity <= 3000:
                recycling_collection = 20000 * 0.17
            elif 3000 < engine_capacity <= 3500:
                recycling_collection = 20000 * 48.5
            else:
                recycling_collection = 20000 * 61.76
        else:
            if 0 <= engine_capacity <= 3000:
                recycling_collection = 20000 * 0.26
            elif 3000 < engine_capacity <= 3500:
                recycling_collection = 20000 * 74.25
            else:
                recycling_collection = 20000 * 81.19
    else:
        if year_left_bound >= current_year - 3 and year_right_bound <= current_year:
            recycling_collection = 20000 * 0.17
        else:
            recycling_collection = 20000 * 0.26
    return recycling_collection
