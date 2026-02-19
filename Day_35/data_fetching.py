#!/usr/bin/env python3
# module data_fetching was built for fetching data from API's sites

import requests,os,pathlib,sys
from dotenv import load_dotenv
import json, time

def inject_api_key():
  path = pathlib.Path.cwd() / '.env' # getting environment data from .env + few alternative ways
  load_dotenv(dotenv_path=path)
  # path = pathlib.Path.cwd() / '.env' # getting environment data from .env + few alternative ways
  # path = os.path.join(os.getcwd(),'.env')
  # if sys.platform == 'win32':
  #   path = fr'{os.getcwd()}\.env'
  #   print(path)
  # elif sys.platform =='linux':
  #   path = f'{os.getcwd()}/.env'
  #   print(path)
  # print(f'1:{sys.version_info}\n, 2:{sys.version}\n, 3:{sys.platform}\n')


def fetching_data():
  # Fetching data from API about weather
  param = {
    "lat":os.getenv('LAT'),
    "lon":os.getenv('LON'),
    "appid":os.getenv('API'),
    "units":"metric",
    "lang":"en"
  }
  with requests.get(url='https://api.openweathermap.org/data/2.5/weather',params=param) as connect:
    print('stat',connect.status_code)
    weather_data=connect.json()
    weather_data_cleaned = json.dumps(weather_data, indent=4,sort_keys=True) # dumps wyrzuca na konsole
  time.sleep(2)
  # Fetching data from API about five days forecast
  with requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=param) as connect1:
    print('stat',connect1.status_code)
    forecast_data=connect1.json()
  return weather_data_cleaned,weather_data,forecast_data

def saving_data(weather_c, weather_d, forecast):
  weather_data_cleaned = weather_c
  weather_data = weather_d
  forecast_data = forecast
  # Saving forecast from my location into files jsondata and jsondata1
  with open(f"{pathlib.Path.cwd() / 'today_weather.json'}",mode='w') as file:
    file.write(weather_data_cleaned) # file.write() expects str not <json_obj> !
  with open(f"{pathlib.Path.cwd() / 'today_weather_1.json'}",mode='w') as file:
    json.dump(weather_data,fp=file, indent=2, sort_keys=True) # dump expects <json_object> not string !

  # Saving five days forecast into file five_days_forecast.json
  with open(f"{pathlib.Path.cwd() / 'five_days_forecast.json'}",mode='w') as file:
    json.dump(forecast_data,fp=file, indent=2, sort_keys=True) # dump expects <json_object> not string !

if __name__ == '__main__': # if you put something here it can't execute in main.py silently and directly too
  pass
  # fetching_data()
  # saving_data(*fetching_data())

# print(json.dumps(forecast_data, indent=2, sort_keys=True))
