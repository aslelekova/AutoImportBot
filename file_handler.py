# file_handler.py
import json
import logging

logger = logging.getLogger(__name__)


def save_to_file(data, filename):
    """
    Save data to a JSON file.

    :param data: The data to be saved.
    :param filename: The name of the file to save the data to.
    :return: None
    """
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error occurred while saving data to file {filename}: {e}")


def load_data_from_json(filename):
    """
    Load data from a JSON file.

    :param filename: The name of the JSON file.
    :return: The loaded data.
    """
    try:
        with open(filename) as file:
            data = json.load(file)
        return data
    except Exception as e:
        logger.error(f"Error occurred while loading data from file {filename}: {e}")
        return None