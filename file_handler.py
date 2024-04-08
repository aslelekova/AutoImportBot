# file_handler.py
import json


def save_to_file(data, filename):
    # Function to save data to a file.
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_data_from_json(filename):
    # Function to load data from a file.
    with open(filename) as file:
        data = json.load(file)
    return data
