# deployed  as a docker container on ubuntu server (pi rasp4)
# own .env file creation needed
# MY_EMAIL=xxx@gmail.com
# MY_EMAIL2=yyy@gmail.com
# MY_EMAIL3=zzz@gmail.com
# MY_PASSWORD=xxxx xxxx xxxx xxxx from account management / app passwords
# MY_HOST=smtp.gmail.com
# MY_PORT=587

import requests, time, pathlib
from datetime import datetime as dt
from dotenv import load_dotenv
import smtplib,os
import socket

MY_LAT=53.710979 # Your latitude
MY_LONG=16.691114 # Your longitude
TIME_OUT=10
D=5.0

dot_path = pathlib.Path.cwd() / '.env' # operator `/` is overloaded as `concatenator` in this library
load_dotenv(encoding='utf-8',dotenv_path=dot_path)
# dot_path=f'{os.getcwd()}\\' #get path, and join \ or /, unfortunately don't care about OS :/, it is what you type
# os.path.join(os.getcwd(),'.env') #this iteral automatically insert / or \ depends on OS, oldest one and most stable
# dot_path = pathlib.Path.cwd() / '.env' #newest and recommended version to handle paths, implemented after python v3.4

# sending mail to recipent(s)
def send_email():
    try:
        with smtplib.SMTP(host=os.getenv('MY_HOST'),port=os.getenv('MY_PORT')) as connect:
            time_now = f"{dt.now().strftime('%H:%M:$S')}"
            connect.starttls()
            connect.login(user=os.getenv('MY_EMAIL'),password=os.getenv('MY_PASSWORD'))
            connect.sendmail(from_addr=os.getenv('MY_EMAIL'),to_addrs=[os.getenv('MY_EMAIL2')],
            msg='Subject:ISS is comming!\n\nInternational Space Station is around 300km from you\nGo outside and LOOK UP! xD')
    except (smtplib.SMTPException, OSError, socket.error) as e:
        print(f'{time_now} [ERROR] We have an error: {e}')
    except Exception as e:
        print(f'{time_now} [ERROR] Something other went wrong: {e}')
    else:
        print(f'[INFO]Email sended !')

# ISS position fetching
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
            print('Is here!')
            return True
        else:
            print('Nope')
            return False

# sunraise and sunset time for my location fetching
def is_dark_now():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": 'Europe/Warsaw'}
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
        print(sunrise_tm.time(),sunset_tm.time(), time_now)
        if sunset_tm.time() < time_now or time_now < sunrise_tm.time():
            print('Night')
            return True
        else:
            print('Day')
            return False

# main loop
is_mail_sended = False # for only one mail purpose
while True:
    if is_dark_now() and is_iss_here():
        if not is_mail_sended: # equivalent of mail_sended == False
            print('It\'s comming !')
            send_email()
            is_mail_sended = True
    else:
        print('Sight contact - negative !')
        is_mail_sended = False

    time.sleep(60)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
