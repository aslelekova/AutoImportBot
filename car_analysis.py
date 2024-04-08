# car_analysis.py
from file_handler import load_data_from_json

def analyze_car_data(data):
    for item in data:
        brand = item.get("vehicle_info", {}).get("mark_info", {}).get("code", "").lower()
        model = item.get("vehicle_info", {}).get("model_info", {}).get("code", "").lower()
        price = item.get("price_info", {}).get("price", "")

        # Получение информации о типе автомобиля (новый или подержанный)
        is_used = item.get("section") == "used"
        complectation_id = item.get("vehicle_info", {}).get("complectation", {}).get("id", "")
        tech_param_id = item.get("vehicle_info", {}).get("tech_param", {}).get("id", "")
        sale_id = item.get("saleId", "")

        # Форматирование базовой части ссылки
        base_link = f"https://auto.ru/cars/"

        # Добавление типа автомобиля (новые или подержанные)
        if is_used:
            base_link += f"used/sale/{brand.lower()}/{model.lower()}/{sale_id}/"
        else:
            base_link += f"new/group/{brand.lower()}/{model.lower()}/{tech_param_id}/{complectation_id}/{sale_id}"

        print("Марка:", brand)
        print("   Модель:", model)
        print("   Цена:", price)
        print("   Ссылка на объявление:", base_link)


    # # Добавление года в ссылку, если он указан
    # if year is not None:
    #     base_link += f"year_{year}/"
    #
    # # Добавление цены в ссылку, если она указана
    # if price is not None:
    #     base_link += f"price_{price}/"
    #
    # # Добавление остальных параметров и ID
    # base_link += f"group/{brand}/{model}/{ad_id}-{sale_id}/"
    #
    # return base_link




# Год и цена задаются пользователем или могут быть None
# year = None
# price = None
#
# # Генерация ссылки с заданными параметрами
# link = generate_car_link(brand, model, ad_id, sale_id, year, price)
# print("Ссылка на объявление:", link)
