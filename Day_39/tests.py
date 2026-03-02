
  # TODO to gówno zacznie działać, dzisiaj xD, no dobra jutro xD

import json

with open('ch_f_v4.json',mode='r') as f:
  data = json.load(fp=f)
  city = data[0]['airports'][0]['arrival'][0]['airport']['name']
  price = data[0]['other_flights'][0]['price']
  dep_airport = data[0]['other_flights'][0]['flights'][0]['departure_airport']['name']
  dep_code = data[0]['other_flights'][0]['flights'][0]['departure_airport']['id']
  departure_date = data[0]['other_flights'][0]['flights'][0]['departure_airport']['time']
  arrival_airport = data[0]['other_flights'][0]['flights'][0]['arrival_airport']['name']
  arr_code = data[0]['other_flights'][0]['flights'][0]['arrival_airport']['id']
  arrival_time = data[0]['other_flights'][0]['flights'][0]['arrival_airport']['time']

  dictionary = {
    f'{city}':{
      "price":f'{price}',
      "depAirport":f'{dep_airport}',
      "depCode":f'{dep_code}',
      "depDate":f'{departure_date}',
      "arrAirport":f'{arrival_airport}',
      "arrCode":f'{arr_code}',
      "arrTime":f'{arrival_time}'
    }
  }
print(dictionary)



  # plik = f.read()
  # print(plik)

# lista = ['zupa','kupa','wiaderko','cycki']
# print(lista)
# print(",".join(lista))
# print(type(",".join(lista)))

# s = "/m/04jpl"
# print(s)
# slownik = {"key1":s}
# print(f'\"{s}\"')

# import json
# give_me_the_disc = []
# with open('kgmid_list.json', mode='r') as f:
#   file = json.load(fp=f)
#   # print(file[0]['suggestions'][0]['airports'])
#   # for data in file[0]['suggestions'][0]['airports']:
#   #   print(data)
#   for data in file:
#     print(data['suggestions'][0]['airports'][0]['city_id'])
#   give_me_the_disc += [data['suggestions'][0]['airports'][0]['city_id'] for data in file]
#
# print(give_me_the_disc) # ! xD

# import os, pathlib, json
# import datetime as dt
# from zoneinfo import ZoneInfo
# from serpapi import GoogleSearch
# from dotenv import load_dotenv
# import json
#
# load_dotenv()
#
# params = {
#   "engine": "google_flights",
#   "departure_id": "CDG",
#   "arrival_id": "AUS",
#   "currency": "USD",
#   "type": "2",
#   "outbound_date": "2026-03-03",
#   "api_key": f"{os.getenv('SERP_API')}"
# }
#
# search = GoogleSearch(params)
# results = search.get_dict()
# with open(file='cycki.json',mode='w') as cycki:
#   json.dump(obj=results,fp=cycki,indent=2,sort_keys=True)
# best_flights = results["best_flights"]
# print(best_flights)


# for entry in price_map:
#     print(f"Data: {entry['date']}, Cena: {entry['price']} PLN")
# with open('iata_data.json',mode='r') as f:
#   js = json.load(fp=f)
#   print(js['cities'][0][0]['iataCode'])
# test_dict = {"zupa":"kalafiorowa","obiad":"obiadowy"}
# print('get',test_dict.get("zupa"))
# print('get',type(test_dict.get("zupa")))
# print('keys',test_dict.keys())
# print('keys',type(test_dict.keys()))
# print('values',test_dict.values())
# print('values',type(test_dict.values()))
# print('items',test_dict.items())
# print('items',type(test_dict.items()))
# file_path = pathlib.Path.cwd() / 'auth_data.json'
# is_file_exist = pathlib.Path.is_file(pathlib.Path.cwd() / 'auth_data.json')
# file_mod_time_unix = os.path.getmtime(file_path)
# file_mod_time_iso = dt.datetime.fromtimestamp(timestamp=file_mod_time_unix, tz=ZoneInfo('Europe/Warsaw'))
# time_now = dt.datetime.now(tz=ZoneInfo('Europe/Warsaw'))
# if is_file_exist:
#   print('token file exists')
#   if (time_now-file_mod_time_iso)>dt.timedelta(minutes=29):
#     print('token expired, generate new one')
#   else:
#     print('token is valid, return token')
# else:
#   print('file doesn\'t exist, generate new file')

# print('time_now',time_now,'file_mod_time_iso',file_mod_time_iso)
# print('time_now',type(time_now),'file_mod_time_iso',type(file_mod_time_iso))
# print('is_file_exist',is_file_exist)
# print('file_mod_time_iso',file_mod_time_iso)
# print('token_age',token_age)
# print('time_now',time_now)
# print('getmtime - get modification time', file_mod_time_unix)
# print('pathlib', pathlib.Path.is_dir(file_path))
# print('pwd_pathlib', file_path)
# t1 = os.path.getatime(file_path)
# t2 = os.path.getctime(file_path)
# pwd_os = os.path.join(os.getcwd(),'auth_data.json')
# print('getatime - get access time',t1)
# print('getctime - get creation time',t2)
# pathlib.Path.is_file()
# pathlib.Path.exists()
# print('pwd_os',pwd_os)
# os.

# ********** TEST IT LATER *****************
# those iterals under this line can help
# r = requests.post(...)
# r.requests.body/headers/url
# r.text/json/headers/status_code

'''
Unfortunately code below doesn't work :)
maybe it needs oauth basic authorization for now I'll use code above
from official requests documentation website

token_getter = requests.Session
token_getter.trust_env = False # disable authentication by .netrc file content
# token_getter_header={
  "Content-Type":"application/x-www-form-urlencoded",
  "grant_type":"client_credentials",
  }
# token_getter_data = {
  "grant_type":"client_credentials",
  "client_id":f"{os.getenv('AMD_APIKEY')}",
  "client_secret":f"{os.getenv('AMD_SECRET')}",
}
# token_getter = requests.post(url=f'{os.getenv('AMD_BASE_URL_GET_TOKEN')}',data=token_getter_data, headers=token_getter_header)
print(token_getter.text)
os.putenv(name=TOKEN,value=)
'''
