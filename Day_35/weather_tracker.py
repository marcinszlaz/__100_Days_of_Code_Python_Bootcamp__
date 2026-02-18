import json, sms_twilio as mt
import data_fetching as s
import whatsup_twilio as t
import datetime as dt

s.inject_api_key()
s.saving_data(*s.fetching_data()) # fetching_data() returns tuple (a,b,c), you have to unpack tuple by * operator
# a,b,c = s.fetching_data() #  more readable alternative
# s.saving_data(a,b,c)

with open('five_days_forecast.json',mode='r') as file:
  weather_data_str = file.read()
  file.seek(0) # without this command we get error, file.seek(0) return from end to begin of the opened file
  weather_data_json = json.load(file)
time_stamp = dt.datetime.now()

will_rain = False
for row in weather_data_json['list'][:4]:
  weather_id = row['weather'][0]['id']
  time_stamp = dt.datetime.fromtimestamp(row['dt'])
  weather_check = f'{time_stamp}',weather_id
  print(weather_check)
  if weather_check[1] < 700:
    will_rain = True

if will_rain:
  print(f'Take an Umbrella ! It may be raining or snowing at: {dt.datetime.strftime(time_stamp,'%H:%M')}')
  msg = '*** It will be rainy day, take an umbrella my child xD ***'
  mt.send_sms(msg)
  t.send_whatsup_msg(msg,time_stamp)

else:
  msg = '*** It will be quite sunny day my child xD ***'
  mt.send_sms(msg)
  t.send_whatsup_msg(msg,time_stamp)

print('you don\'t have to concern about weather')

# for _ in range(0,(int(len(weather_data_json['list'])/10))):
#   weather_id = weather_data_json['list'][_]['weather'][0]['id']
#   time_stamp = dt.datetime.fromtimestamp(weather_data_json['list'][_]['dt'])
#   weather_check = f'{time_stamp}',weather_id
#   if weather_check[1] < 700:
#     print(f'Take an Umbrella ! It may be raining or snowing at: {dt.datetime.strftime(time_stamp,'%H:%M')}')
#     break

# print(f'{weather_data_json['list'][::20]}')
# list = f'{weather_data_json['list'][::20]}'
# print(len(weather_data_json['list'][::20]))

# with open('five_days_forecast.json',mode='r') as file:
#   weather_data_json = json.load(file)
# print(weather_data_str)
# print(type(weather_data_str))
# print(weather_data_json)
# print(type(weather_data_json))