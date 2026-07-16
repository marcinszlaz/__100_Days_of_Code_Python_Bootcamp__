# import numpy as np
# import pandas as pd
#
# test_list = [1,2,3,4,5]
#
# print('test_list: ',test_list)
# print('test_list reversed: ',test_list[::-1])
#
# maciorka = np.array([
#
#   [[1,2,3],
#   [4,5,6],
#   [7,8,9]],
#   [[1,2,3],
#   [4,5,6],
#   [7,8,9]],
#   [[1,2,3],
#   [4,5,6],
#   [7,8,9]]
#
# ])
#
#
# print('maciorka\n', maciorka)
# print('.ndim', maciorka.ndim)
# print('.shape', maciorka.shape)
#
# reverted_maciorka = maciorka[:,::-1,:]
# print('reverted maciorka: \n', reverted_maciorka)
#
# eg = pd.read_csv('egzample.csv')
# print(eg)
# eg.to_excel(excel_writer = './egzample.xlsx', index = False)
#
# # import pandas as pd
# #
# # # Przykładowe dane
# # df = pd.DataFrame({'Produkt': ['Laptop', 'Mysz', 'Monitor'], 'Cena': [3000, 50, 800]})
# #
# # # 1. Tworzymy silnik ExcelWriter
# # with pd.ExcelWriter('raport.xlsx', engine='xlsxwriter') as writer:
# #   df.to_excel(writer, sheet_name='Sprzedaż', index=False)
# #
# #   # 2. Pobieramy dostęp do arkusza i skoroszytu
# #   workbook = writer.book
# #   worksheet = writer.sheets['Sprzedaż']
# #
# #   # 3. Definiujemy formaty
# #   format_header = workbook.add_format({'bold': True, 'bg_color': '#D3D3D3', 'border': 1})
# #   format_money = workbook.add_format({'num_format': '#,##0.00 zł'})
# #
# #   # 4. Nakładamy formaty
# #   # Ustawiamy szerokość kolumn
# #   worksheet.set_column('A:A', 20)
# #   worksheet.set_column('B:B', 15, format_money)
# #
# #   # Formatujemy nagłówki (A1:B1)
# #   for col_num, value in enumerate(df.columns.values):
# #     worksheet.write(0, col_num, value, format_header)
#
# from contextlib import contextmanager
#
# import pandas as pd
#
# slownik = dict(
#                 age=[5, 6, np.nan],
#                 born=[
#                     pd.NaT,
#                     pd.Timestamp("1939-05-27"),
#                     pd.Timestamp("1940-04-25"),
#                 ],
#                 name=["Alfred", "Batman", ""],
#                 toy=[None, "Batmobile", "Joker"],
#                 titties=('cyka','blyat','nyah'),
#             )
#
# print(slownik)
# print(type(slownik['age']))
# print(type(slownik['titties']))
# df = pd.DataFrame(data = (slownik))
# print(df)
# print(df.columns)
# d = dict(name = '', name_1 = '')
# print(d)
# dd = dict([('%','.'),(',','.')])
# print(dd)
#
# import random as r
#
# print(r.sample(population = range(1,50),k = 6))
#
print(10%4)