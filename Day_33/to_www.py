# script will be deployed at https://www.pythonanywhere.com
#TODO


#4 wrzuc to na stronke, sprawdz czy dziala z stronki
#5 wrzuc jako unit w systemd, stwórz env
#6 wrzuć jako docker, stwórz do tego image, bez docker file, sam gotowy image do odpalenia na życzenie


import requests, time, pathlib
from datetime import datetime as dt
from dotenv import load_dotenv
import smtplib,os

MY_LAT=53.710979 # Your latitude
MY_LONG=16.691114 # Your longitude
TIME_OUT=5
D=5.0

dot_path = pathlib.Path.cwd() / '.env' # operator `/` is overloaded as `concatenator` in this library
load_dotenv(encoding='utf-8',dotenv_path=dot_path)
# dot_path=f'{os.getcwd()}\\' #get path, and join \ or /, unfortunately don't care about OS :/, it is what you type
# os.path.join(os.getcwd(),'.env') #this iteral automatically insert / or \ depends on OS, oldest one and most stable
# dot_path = pathlib.Path.cwd() / '.env' #newest and recommended version to handle paths, implemented after python v3.4


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": 'Europe/Warsaw'
}

# sending mail to recipent(s)
def send_email():
    with smtplib.SMTP(host=os.getenv('MY_HOST'),port=os.getenv('MY_PORT')) as connect:
        connect.starttls()
        connect.login(user=os.getenv('MY_EMAIL'),password=os.getenv('MY_PASSWORD'))
        connect.sendmail(from_addr=os.getenv('MY_EMAIL'),to_addrs=[os.getenv('MY_EMAIL2')],
        msg='Subject:ISS is comming!\n\nInternational Space Station is around 300km from you\nGo outside and LOOK UP! xD')
        # connect.close() # yes, I'm aware about trick with `with as` ;)

# ISS position fetching (getting)
def is_iss_here():
    global D,MY_LAT,MY_LONG
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=TIME_OUT)
        response.raise_for_status()
    except requests.RequestException as re:
        print(f'Internet connection failure, error code: {re}')
        return False
    except Exception as re:
        print(f'Something other went terribly wrong, error cod: {re}')
    else:
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])
        print(iss_latitude,iss_longitude)
        if (MY_LAT-D)<=iss_latitude<=(MY_LAT+D) and (MY_LONG-D)<=iss_longitude<=(MY_LONG+D):
            return True
        else:
            return False

# sunraise and sunset time for my location fetching (getting)
def is_dark_now():
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=TIME_OUT)
        response.raise_for_status()
    except requests.RequestException as er:
        print(f'Internet connection failure, error code: {er}')
        return False
    except Exception as er:
        print(f'Something other went terribly wrong, error code: {er}')
        return False
    else:
        data = response.json()
        sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
        sunset = data["results"]["sunset"].split("T")[1].split("+")[0]
        time_now = dt.now().time()
        sunrise_tm = dt.strptime(sunrise,'%H:%M:%S')
        sunset_tm = dt.strptime(sunset,'%H:%M:%S')
        print(sunrise_tm,sunset_tm)
        if sunset_tm.time() < time_now < sunrise_tm.time():
            return True
        else:
            return False

# main loop
mail_sended = False
while True:
    if is_dark_now():
        if is_iss_here():
            if not mail_sended: # equivalent of mail_sended == False
                print('It\'s comming !')
                send_email()
                mail_sended = True
    else:
        print('Sight contact - negative !')
        mail_sended = False

    time.sleep(60)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
