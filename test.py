import json
import math

import requests
import tqdm

from config import url_encar_com, headers_encar_com
from file_handler import save_to_file


def parse_encar_com():
    params ={ "count": "true",
    "q": "(And.Hidden.N._.CarType.Y.)",
    "sr": "|ModifiedDate|20|20"
              }
    all_data = []

    response = requests.get(url_encar_com, params=params, headers=headers_encar_com)
    if response.status_code == 200:
        try:
            json_data = response.json()
            count = json_data.get("Count", 0)
            total_pages = math.ceil(count / 20)

            for page in tqdm.tqdm(range(total_pages)):
                params["sr"] = f"|ModifiedDate|{page * 20}|20"
                response = requests.get(url_encar_com, params=params, headers=headers_encar_com)
                if response.status_code == 200:
                    try:
                        json_data = response.json()
                        all_data.append(json_data)
                    except json.decoder.JSONDecodeError:
                        print("Ошибка: Невозможно преобразовать ответ в JSON")
                        break
                else:
                    print(f"Ошибка: Не удалось выполнить запрос. Код ответа: {response.status_code}")
                    break

        except json.decoder.JSONDecodeError:
            print("Ошибка: Невозможно преобразовать ответ в JSON")
    else:
        print(f"Ошибка: Не удалось выполнить запрос. Код ответа: {response.status_code}")
    return all_data


parse_encar_com()

offers_data_encar_com = parse_encar_com()

# Saving the parsed data to a file.
save_to_file(offers_data_encar_com, "data.json")