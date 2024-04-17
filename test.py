import json
import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru',
    'Connection': 'keep-alive',
    'Host': 'api.encar.com',
    'Origin': 'http://www.encar.com',
    'Referer': 'http://www.encar.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15'
}

url = "http://api.encar.com/search/car/list/premium"
params = {
                 "count": "true",
                 "q": "(And.Mileage.range(10000..150000)._.Hidden.N._.(C.CarType.N._.(C.Manufacturer.람보르기니._.ModelGroup.아벤타도르.))_.FuelType.가솔린._.Year.range(..).)",
                 "sr": "|ModifiedDate|0|20"
    }
response = requests.get(url, params=params, headers=headers)


# Проверка на успешность запроса
if response.status_code == 200:
    try:
        # Попытка преобразовать ответ в JSON
        json_data = response.json()
        # Сохранение в файл, если удалось преобразовать в JSON
        with open("encar.json", "w") as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)
    except json.decoder.JSONDecodeError:
        print("Ошибка: Невозможно преобразовать ответ в JSON")
else:
    print(f"Ошибка: Не удалось выполнить запрос. Код ответа: {response.status_code}")
