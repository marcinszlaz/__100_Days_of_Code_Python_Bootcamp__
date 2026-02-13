import time
import requests
import datetime as dt

# long / lat get
long_lat = requests.get(url='http://api.open-notify.org/iss-now.json')
long_lat.raise_for_status()
longitude = long_lat.json()['iss_position']['longitude']
latitude = long_lat.json()['iss_position']['latitude']
iss_position = (latitude,longitude)
print('pobrana dlugosc i szerokosc geograficzna miedzynarodowej stacji kosmicznej',iss_position)

# sunrise time get
param ={'lat':latitude,'lng':longitude,'formatted':0}
param1 ={'formatted':0}

get_sun_umniexD = requests.get(url='https://api.sunrise-sunset.org/json?lat=53.710979&lng=16.691114',params=param1) #Neustettin :)
get_sun_umniexD.raise_for_status()
print('wschod slonca Sz-ek',get_sun_umniexD.json()['results']['sunset'])
print('zachod slonca Sz-ek',get_sun_umniexD.json()['results']['sunrise'])
time.sleep(1)

# get_sun.raise_for_status()
get_sun = requests.get(url='https://api.sunrise-sunset.org/json', params=param)
print('sunrise MIR2',get_sun.json()['results']['sunset'])
print('sunset MIR2',get_sun.json()['results']['sunrise'])
print('sunset MIR2 pociety',(get_sun.json()['results']['sunrise']).split('T')[1].split('+')[0])
time = (get_sun.json()['results']['sunrise']).split('T')[1].split('+')[0]

print(dt.datetime.now().time())