# import requests
# import json
#
# def get_data(url, output_file):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }
#
#     req = requests.get(url, headers)
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.write(req.text)
#
# get_data("https://auto.ru", "auto_ru_data.html")

#     with open("index.html") as file:
#         file.write()
# with open("index.html") as file:
#     src = file.read()

#
# # Ищем все элементы <a> с классом "IndexMarks__item"
# all_links = soup.find_all('a', class_='IndexMarks__item')
#
# all_categories_dict = {}
# # Проходимся по найденным элементам и извлекаем ссылки и названия
# for link in all_links:
#     car_name = link.find('div', class_='IndexMarks__item-name').text.strip()
#     car_link = link['href']
#     all_categories_dict[car_name] = car_link
#
# with open("all_categories_dict.json", "w") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

# main.py
from data_parser import parse_auto_ru
from file_handler import save_to_file


def main():
    offers_data = parse_auto_ru()
    save_to_file(offers_data, "data.json")


if __name__ == "__main__":
    main()
