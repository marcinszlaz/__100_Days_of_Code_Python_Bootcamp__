import requests, time
from datetime import datetime as dt
from dotenv import load_dotenv
import smtplib,os

MY_LAT = 53.710979 # Your latitude
MY_LONG = 16.691114 # Your longitude
load_dotenv()

#Your position is within +3 or -3 degrees of the ISS position.
def send_email():
    connect = smtplib.SMTP(host=os.getenv('MY_HOST'), port = os.getenv('MY_PORT'))
    connect.starttls()
    connect.login(user=os.getenv('MY_EMAIL'),password=os.getenv('MY_PASSWORD'))
    connect.sendmail(from_addr=os.getenv('MY_EMAIL'),to_addrs=[os.getenv('MY_EMAIL2'),os.getenv('MY_EMAIL3')],
    msg='Subject:ISS is comming!\n\nInternational Space Station is around 300km from you\nGo outside and LOOK UP! xD')
    connect.close() # yes, I'm aware about trick with `with as` ;)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": 'Europe/Warsaw'
}

while True:
    # ISS position fetching (getting)
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # sunraise and sunset time for my location fetching (getting)
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
    sunset = data["results"]["sunset"].split("T")[1].split("+")[0]

    time_now = dt.now().time()
    sunrise_tm = dt.strptime(sunrise,'%H:%M:%S')
    sunset_tm = dt.strptime(sunset,'%H:%M:%S')

    if  (((MY_LAT-3.0) <= iss_latitude <= (MY_LAT+3.0))
        and ((MY_LONG-3.0) <= iss_longitude <= (MY_LONG+3.0))
        and sunset_tm.time() < time_now < sunrise_tm.time()):
        print('It\'s comming !')
        send_email()
    else:
        pass
    time.sleep(60)


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
