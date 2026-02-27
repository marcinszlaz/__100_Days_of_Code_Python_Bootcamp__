import os, pathlib, json
import datetime as dt
from zoneinfo import ZoneInfo

with open('iata_data.json',mode='r') as f:
  js = json.load(fp=f)
  print(js['cities'][0][0]['iataCode'])

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
