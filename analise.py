# analise.py
from file_handler import load_data_from_json

data = load_data_from_json("data.json")
for item in data:
    ad_id = item.get("id", "")
    print("Ссылка на объявление:", ad_id)


#
# price = []
# for offer in data:
#     if offer.get('price_info'):
#         price.append(offer['price_info']['price'])
# print(price)
