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
