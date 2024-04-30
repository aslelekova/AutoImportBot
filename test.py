# import numpy as np
# from scipy.spatial.distance import euclidean
#
#
# encoded_data_encar_com = {'http://www.encar.com/dc/dc_cardetailview.do?carid=37021400': [5198570.81, 95895.0, '2019', 0, 1, 0, 0]}
#
# encoded_data_auto_ru = {'<a href="https://auto.ru/cars/used/sale/bmw/x5/1122962941-a547a3a5/">BMW X5 IV (G05/G18) '
#                         '2019</a>': [6765000, 82300, 2019, 1, 0, 0, 0],
#                         '<a href="https://auto.ru/cars/used/sale/bmw/x5/1122051172-f2ff6396/">BMW X5 IV (G05/G18) '
#                         '2020</a>': [7249000, 85020, 2020, 0, 1, 0, 0],
#                         '<a href="https://auto.ru/cars/used/sale/bmw/x5/1120611685-f6777e6f/">BMW X5 IV (G05/G18) '
#                         '2021</a>': [10400000, 6800, 2021, 1, 0, 0, 0],
#                         '<a href="https://auto.ru/cars/used/sale/bmw/x5/1122358235-838a3bed/">BMW X5 IV (G05/G18) '
#                         '2019</a>': [6399000, 70000, 2019, 1, 0, 0, 0],
#                         '<a href="https://auto.ru/cars/used/sale/bmw/x5/1123173051-e7afc140/">BMW X5 IV (G05/G18) '
#                         '2019</a>': [7999000, 63000, 2019, 1, 0, 0, 0],
#                         '<a href="https://auto.ru/cars/used/sale/bmw/x5/1122796566-01b5fe27/">BMW X5 IV (G05/G18) '
#                         '2021</a>': [9390000, 63086, 2021, 1, 0, 0, 0]}
#
# top_3_closest_cars = compare_cars_encar_auto_ru(encoded_data_encar_com, encoded_data_auto_ru)
# print(top_3_closest_cars)