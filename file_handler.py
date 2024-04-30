# file_handler.py
import json


def save_to_file(data, filename):
    """
    Save data to a JSON file.

    :param data: The data to be saved.
    :param filename: The name of the file to save the data to.
    :return: None
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_data_from_json(filename):
    """
    Load data from a JSON file.

    :param filename: The name of the JSON file.
    :return: The loaded data.
    """
    with open(filename) as file:
        data = json.load(file)
    return data
