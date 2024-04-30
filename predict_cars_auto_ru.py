import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean
from sklearn.preprocessing import StandardScaler


def encode_fuel_type(data):
    # Создаем DataFrame из данных
    df = pd.DataFrame(data.values(), columns=["Price", "Mileage", "Fuel Type", "Year"], index=data.keys())

    # Преобразуем категориальную переменную 'Fuel Type' в числовое представление с помощью One-Hot Encoding
    fuel_types = ['GASOLINE', 'DIESEL', 'ELECTRO', 'HYBRID']
    for fuel_type in fuel_types:
        df[f'Fuel Type_{fuel_type}'] = df['Fuel Type'].apply(lambda x: 1 if x == fuel_type else 0)
    df.drop(columns=['Fuel Type'], inplace=True)

    # Возвращаем результат в виде словаря
    encoded_data = {}
    for key, row in df.iterrows():
        encoded_data[key] = row.values.tolist()

    return encoded_data


def normalize_data_dict(data_dict):
    scaler = StandardScaler()
    # Создаем список векторов из значений словаря
    vectors = list(data_dict.values())
    # Подгоняем StandardScaler к данным
    scaler.fit(vectors)
    # Применяем нормализацию ко всем векторам
    normalized_vectors = scaler.transform(vectors)
    # Заменяем значения в словаре нормализованными векторами
    for key, vector in zip(data_dict.keys(), normalized_vectors):
        data_dict[key] = vector
    return data_dict


def compare_cars_encar_auto_ru(encoded_data_encar_com, encoded_data_auto_ru):
    similarity_list = []
    for car_encar, vector_encar in encoded_data_encar_com.items():
        for car_auto_ru, vector_auto_ru in encoded_data_auto_ru.items():
            try:
                # Convert strings to numerical values
                vector_encar = np.array(vector_encar, dtype=float)
                vector_auto_ru = np.array(vector_auto_ru, dtype=float)
                # Calculate Euclidean distance
                distance = euclidean(vector_encar, vector_auto_ru)
                similarity_list.append((car_auto_ru, distance))
            except ValueError:
                print(f"Skipping comparison between {car_encar} and {car_auto_ru} due to incompatible types")

    # Sort by distance and get top 3 closest cars
    sorted_similarity_list = sorted(similarity_list, key=lambda x: x[1])
    top_3_closest = sorted_similarity_list[:3]

    if top_3_closest:
        return [car[0] for car in top_3_closest]
    else:
        return "Эта машина - эксклюзив!"
