import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean
from sklearn.preprocessing import StandardScaler
import logging

logger = logging.getLogger(__name__)


def encode_fuel_type(data):
    """
    Encode fuel types into numerical representations using One-Hot Encoding.

    :param data: A dictionary containing car data.
    :return: A dictionary containing encoded car data.
    """
    # Create a DataFrame from the data.
    df = pd.DataFrame(data.values(), columns=["Power", "Volume", "Mileage", "Fuel Type", "Year"], index=data.keys())

    # Convert the categorical variable 'Fuel Type' into numerical representation using One-Hot Encoding.
    fuel_types = ['GASOLINE', 'DIESEL', 'ELECTRO', 'HYBRID']
    for fuel_type in fuel_types:
        df[f'Fuel Type_{fuel_type}'] = df['Fuel Type'].apply(lambda x: 1 if x == fuel_type else 0)
    df.drop(columns=['Fuel Type'], inplace=True)

    # Return the result as a dictionary.
    encoded_data = {}
    for key, row in df.iterrows():
        encoded_data[key] = row.values.tolist()

    return encoded_data


def normalize_data_dict(data_dict):
    """
    Normalize the values in the dictionary.

    :param data_dict: A dictionary containing car data.
    :return: A normalized dictionary of car data.
    """
    scaler = StandardScaler()
    vectors = list(data_dict.values())

    # Fit the StandardScaler to the data.
    scaler.fit(vectors)

    # Apply normalization to all vectors.
    normalized_vectors = scaler.transform(vectors)

    # Replace values in the dictionary with normalized vectors.
    for key, vector in zip(data_dict.keys(), normalized_vectors):
        data_dict[key] = vector

    return data_dict


def compare_cars_encar_auto_ru(encoded_data_encar_com, encoded_data_auto_ru):
    """
    Compare cars from encar.com and auto.ru based on encoded data.

    :param encoded_data_encar_com: Encoded car data from encar.com.
    :param encoded_data_auto_ru: Encoded car data from auto.ru.
    :return: A list of top 3 closest cars from auto.ru for each car from encar.com.
    """

    similarity_list = []

    for car_encar, vector_encar in encoded_data_encar_com.items():
        for car_auto_ru, vector_auto_ru in encoded_data_auto_ru.items():
            try:
                # Convert strings to numerical values.
                vector_encar = np.array(vector_encar, dtype=float)
                vector_auto_ru = np.array(vector_auto_ru, dtype=float)
                # Calculate Euclidean distance.
                distance = euclidean(vector_encar, vector_auto_ru)
                similarity_list.append((car_auto_ru, distance))
            except ValueError:
                logging.error(f"Skipping comparison between {car_encar} and {car_auto_ru} due to incompatible types")
                pass

    # Sort by distance and get top 3 closest cars.
    sorted_similarity_list = sorted(similarity_list, key=lambda x: x[1])
    top_3_closest = sorted_similarity_list[:3]

    return [car[0] for car in top_3_closest] if top_3_closest else []


# Configure logging
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
