import json

with open("data.json", "r", encoding="utf8") as f:
    data = json.load(f)

price = []
x = 1
for offer in data:
    if offer['price_info']:

        price.append(offer['price_info']['price'])
print(price)
# average = sum(price) / len(price)
# print("Average: ", int(average))