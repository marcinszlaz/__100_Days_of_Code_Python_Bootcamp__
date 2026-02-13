import time
import requests

# iterator = 0
# while iterator < 10:
#   ping = requests.get(url='http://api.open-notify.org/iss-now.json')
#   time.sleep(1)
#   print(ping.content)
#   iterator += 1


ping = requests.get(url='http://api.open-notify.org/iss-now.json')
if ping.status_code == 404:
  raise Exception('That resource doesn\'t  exist.')
elif ping.status_code == 401:
  raise Exception('You aren\'t authorised to access this data.')

ping.raise_for_status()
data = ping.json()
print(data)
longitude = data["iss_position"]['longitude']
latitude = data['iss_position']['latitude']
iss_position=(longitude, latitude)
print(iss_position)
