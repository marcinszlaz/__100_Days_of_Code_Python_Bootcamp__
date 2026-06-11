# playing with MicroTik REST API
# to input password you have run script from terminal (ctrl `)

import sys, os, pathlib
from dotenv import load_dotenv
import json
import requests, getpass
from requests.auth import HTTPBasicAuth
import urllib3


urllib3.disable_warnings() # disable ssl warnings, I hope you know what you're doing ;)
dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path = dotenv_path)

'''

'''


# sys.stdout.write('lubie'+' '+'mariole od matmy')
temp = sys.stdout
sys.stdout = open('plik.txt','w')
for _  in range(1,11,2):
  print(_)
sys.stdout = temp # standard output back to defaults


file = open('./response.txt','r')
# print(file.read())
file.close()

with open(file = './response.txt', mode = 'r', encoding = 'utf-8') as response:
  druk = json.load(response)
  formatted_druk = json.dumps(druk,indent=4,sort_keys = True)
  # print(formatted_druk)

URL = 'https://10.215.14.1/rest/ip/arp'
# LOGIN = input('Podaj login: ')
PASS = getpass.getpass("Podaj hasło: ")
LOGIN = os.getenv('LOGIN')
# PASS = os.getenv('PASS')

response = requests.get(
  url = URL,
  auth = HTTPBasicAuth(username = LOGIN, password = PASS),
  timeout = 5,
  verify = False
)

formatted_response = json.dumps(response.json(), indent=4, sort_keys=True)
# print((formatted_response))

interface = '1 Internet' # this is ignored, you have make if statement after {searching patter}
for key in response.json():
  match key:
    case {'address':host_ip, 'mac-address':mac,'interface':interface} if interface == '1 Internet':
      print(host_ip,mac, interface)

response = requests.get(
  url = 'https://10.215.14.1/rest/log',
  auth = HTTPBasicAuth(username = LOGIN, password = PASS),
  timeout = 5,
  verify = False
)
print(json.dumps(response.json(), indent=4, sort_keys=True))

