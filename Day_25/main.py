import pandas
from sqlalchemy import create_engine
import csv
import pandas as df
from prettytable import PrettyTable
import math
import statistics

engine = create_engine('mysql+pymysql://winuser:winuser@10.215.14.30:3306/csv_testy')
#
# csv_as_list = []
#
# with open('weather_data.csv',mode = 'r') as weather:
#   weather_data_imp = []
#   weather_data = weather.readlines()
#   for w_d in weather_data:
#     weather_data_imp.append(w_d.replace('\n',''))
#
# # print("csv file as list, without \'whitespaces\'",weather_data_imp)
#
# with open('weather_data.csv',mode='r') as csv_file:
#   csv_file_content = csv.reader(csv_file)
#   # csv_as_list = list(csv_file_content) # jak wczytasz obiekt (iterator) do listy to on się skończy i już nic nie
#   # wydrukujesz z tej pętli poniżej, musialbyś iterować z listy a nie z obiektu, bo te obiekty są napisane do dużych
#   # ilości danych i nie ładują wszystkiego do RAM, tylko biorą po kawałeczku (po lini) coś jak generator yield
#   for row in csv_file_content:
#     print(row)
#   print(csv_file_content)
#
# print(csv_as_list)
#
# with open('weather_data.csv',mode='r') as file:
#   data = csv.reader(file) # csv.reader() jest o tyle sprytny, ze nie wczytuje calego pliku do ram
# #oszczedza pamiec, a normalnie open() wczytuje calosc, przy duzych plikach to ma duże znaczenie dla wydajności
# #csv.reader tworzy obiekt iterowalny, można w nim przesuwać sie w poszukiwaniu linijek, po uzyciu znika, nie można
# #sie do niego więcej odwołać
#   temperatures =[]
#   for row in data:
#     if  row[1] != 'temp':
#       temperatures.append(int(row[1]))
#     print(row)
#   print(temperatures)
#   print(sum(temperatures))
#   print(f'{sum(temperatures)/len(temperatures):.3f}')
#
# print('obiekt csv.reader w pamieci, ma taki adres a to sa konwersje',(bin(0x000001FEC843DCC0),oct(0x000001FEC843DCC0),
#       int(0x000001FEC843DCC0), float(0x000001FEC843DCC0)))
#
# # zamiast całego kodu powyżej od 25 lini, można użyć pandy xD
# # instalacja pandy w venv pycharm ctrl ` [konsola] pip install pandas, aktualizacja pip
# # python.exe -m pip install --upgrade pip
#
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# table = PrettyTable() # instalacja prettytable ctrl ` pip install prettytable, tylko w venv, konstruktor
# table.field_names = data.columns.tolist() # field nejmy = data z panda, columny, tolist() zmienia specjalny format dan
# #ych z pandy na zwykla liste czytelna dla prettytable, obiekty pandas sa niezrozumialem dla pretty
# table.add_rows(data.values.tolist()) # obiekt tabelka dodaje rowy xD jako argument dostaje values z obiektu
# # data zmienione w stadnardowa pythonowa liste
# # print(table)
#
# # mierzymy srednia temperature z kolumy temperatura
#
# print(data['day'].values)
# print(f'srednia temperatura: {data['temp'].mean():.3f}')
# print(data['temp'].describe())
# print(data['temp'].max())
# print(data.temp) # tak też można dostać do kolumny, drukuje z indexami
#
# # how to get rows ?
# print(data[data.day == "Monday"]) # to jest świetne :)
# # which day of week has the highest temperature :)
#
# print('The day with the highest temperature: \n',data[data.temp == data.temp.max()])
# print('The day with the highest temperature: \n',data[data.temp == data['temp'].max()]) # to x kropką jest trochę myl
# # ące
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(f'Temperatura w poniedziałek {monday.temp[0] * 1.8 + 32} stopni fahrenhaita')
# monday_temp = monday.temp
# print(monday_temp)
#
# # How to create dataframe from scratch ?
# # np z dict
#
# data_dict = {
#   "students": ["Amy","James","Angela"],
#   "scores": [76, 56, 65]
# }
# print(data_dict)
# data = pandas.DataFrame(data_dict) # bardzo prosty sposob zeby np slownik przerobic na dataframe a potem dataframe w csv
# data.to_csv("new_data.csv")

sqd = df.read_csv("squrwiels.csv")
# print(squirrel_data)
# print(sqd.columns[sqd.columns == 'Primary Fur Color'])
print(sqd.columns[sqd.columns == 'Primary Fur Color'])
# sqd.to_sql(name='squirrel_data', con=engine, if_exists='replace', index=False) # tak sie wlasnie zapisuje csv do
# db w mysql xD
etap1 = (sqd['Primary Fur Color']).value_counts().reset_index() # obiekt sqd ma w sobie przeczytany csv z wiewiórkami
# wybierasz kolumne prmary fur color funkcja value_counts to cos jak COUNT(*) z SQL, reset_index() wywala kolumne z indexami
etap1.columns =['Fur Color','Count'] # tym sie nazywa kolumny
etap1.to_csv('jedna_kolumna.csv', index = False) # index = False to csv usuwa kolumne z indexami

# metoda inna xD

sqd1 = df.read_csv("squrwiels.csv")

# print(sqd1['Primary Fur Color'])
gray_count = len(sqd1[sqd1['Primary Fur Color'] == "Gray"])
cinnamon_count = len(sqd1[sqd1['Primary Fur Color'] == "Cinnamon"])
black_count = len(sqd1[sqd1['Primary Fur Color'] == "Black"])

print(black_count)

sq_dict= {
  "Fur Color":["Gray","Cinnamon","Black"],
  "Count":[gray_count, cinnamon_count, black_count]
}

sq_df = pandas.DataFrame(sq_dict)
sq_df.to_csv('one_col.csv')