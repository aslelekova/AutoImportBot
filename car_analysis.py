# car_analysis.py
import locale
from random import sample, random

from aiogram.utils.markdown import hbold, hlink


def analyze_car_data_auto_ru(data_auto_ru):
    prices = []
    links_auto_ru = []
    for item in data_auto_ru:
        # Extracting brand, model, and price information from the data.
        brand = item.get("vehicle_info", {}).get("mark_info", {}).get("code", "").lower()
        model = item.get("vehicle_info", {}).get("model_info", {}).get("code", "").lower()
        generation_auto_ru = item.get("vehicle_info", {}).get("super_gen", {}).get("name", "").lower()
        year_auto_ru = item.get("documents", {}).get("year", {})
        price_rub = item.get("price_info", {}).get("price", "")
        prices.append(price_rub)

        # Getting information about whether the car is new or used.
        is_used = item.get("section") == "used"
        complectation_id = item.get("vehicle_info", {}).get("complectation", {}).get("id", "")
        tech_param_id = item.get("vehicle_info", {}).get("tech_param", {}).get("id", "")
        sale_id = item.get("saleId", "")

        base_link_auto_ru = create_link_auto_ru(brand, model, sale_id, tech_param_id, complectation_id, is_used, generation_auto_ru, year_auto_ru)
        links_auto_ru.append(base_link_auto_ru)

        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        prices = [price for price in prices if price]
        average_price = sum(prices) / len(prices)
        formatted_average_price = locale.format_string("%.0f", average_price, grouping=True)

    return brand, model, formatted_average_price, links_auto_ru


def analyze_car_data_encar_com(data_encar_com, brand, model, formatted_average_price, links_auto_ru):
    cards = []
    for page_data in data_encar_com:
        for item in page_data.get("SearchResults", []):
            id = item.get("Id", "")
            generation_encar_com = item.get("Badge", "")
            mileage = item.get("Mileage", "")
            formatted_mileage = '{:,.0f}'.format(mileage).replace(',', ' ')
            price_won = item.get("Price", "")
            locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
            formatted_price_won = '{:,.0f}'.format(price_won * 10000).replace(',', ' ')
            year_encar_com = str(item.get("Year", ""))[:4]
            base_link_encar_com = f"http://www.encar.com/dc/dc_cardetailview.do?carid={id}"
            card = create_card(brand, model, generation_encar_com, year_encar_com, base_link_encar_com, formatted_mileage, formatted_price_won, formatted_average_price,
                links_auto_ru)
            cards.append(card)
    return cards


def create_link_auto_ru(brand, model, sale_id, tech_param_id, complectation_id, is_used, generation_auto_ru, year_auto_ru):
    # Formatting the base part of the link.
    base_link = f"https://auto.ru/cars/"

    # Adding type of the car (new or used) to the link.
    if is_used:
        base_link += f"used/sale/{brand.lower()}/{model.lower()}/{sale_id}/"
    else:
        base_link += f"new/group/{brand.lower()}/{model.lower()}/{tech_param_id}/{complectation_id}/{sale_id}"

    link = hlink(f'{brand.upper()} {model.title()} {generation_auto_ru.upper()} {year_auto_ru}', base_link)
    return link


# ₽
def create_card(brand, model, generation_encar_com, year_encar_com, base_link_encar_com, formatted_mileage, formatted_price_won, formatted_average_price,
                links_auto_ru):
    card = (
        f"{hlink(f'{brand.upper()} {model.title()} {generation_encar_com.upper()} {year_encar_com}', base_link_encar_com)}\n\n"
        f"{hbold('Пробег: ')} {formatted_mileage} км\n"
        f"{hbold('Год выпуска: ')} {year_encar_com}\n\n"
        f"{hbold('Цена в вонах: ')} {formatted_price_won} ₩\n"
        f"{hbold('Цена привоза под ключ: ')} 3000 ₽\n"
        f"{hbold('Средняя цена в России: ')} {formatted_average_price} ₽\n\n"
        f"{hbold('Похожие объявления в России: ')}\n"
        f"{get_random_links(links_auto_ru)}"
    )
    return card


def get_random_links(links_auto_ru):
    random_links = sample(links_auto_ru, 3)

    return (
        f"1. {random_links[0]}\n"
        f"2. {random_links[1]}\n"
        f"3. {random_links[2]}"
    )