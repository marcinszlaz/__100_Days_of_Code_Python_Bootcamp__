import smtplib,os
from twilio.rest import Client
import pathlib
from dotenv import load_dotenv
import datetime as dt
import socket

'''
SCRIPT REQUIREMENTS the following data in .env file:

# twilio data
PHONE=_____YOUR_PHONE_NUMBER
MSG_SRV_SID=______YOUR_MESSAGE_SERVICE(SERVER)_SID
ACC_SID=_____YOUR_ACCOUNT_SID
AH_TOK=_____YOUR_AUTHORIZATION_TOKEN

#whatsup data
#ACC_SID=_____YOUR_ACCOUNT_SID
#AH_TOK=_____YOUR_AUTHORIZATION_TOKEN
CONTENT_SID=____YOUR_CONTENT_SID
TO=whatsapp:+48_____YOUR_PHONE_NUMBER

# data for smtplib
MY_EMAIL=____YOUR_EMAIL_ADDRESS__@gmail.com
MY_PASSWORD=___YOUR_APPLICATION_PASSWORD
MY_HOST=smtp.gmail.com
MY_PORT=587
'''

class NotificationManager:
  """This class is responsible for sending notifications with the deal flight details."""
  def __init__(self):
    #self.load_var() # uncomment if required
    pass

  def load_var(self)->None:
    dotenv_path = pathlib.Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

  def send_email(self,subject: str,message: str):
    """sending an email"""
    try:
      with smtplib.SMTP(host=os.getenv('MY_HOST'), port=os.getenv('MY_PORT')) as connect:
        time_now = f"{dt.datetime.now().strftime('%H:%M:$S')}"
        connect.starttls()
        connect.login(user=os.getenv('MY_EMAIL'), password=os.getenv('MY_PASSWORD'))
        connect.sendmail(from_addr=os.getenv('MY_EMAIL'), to_addrs=[os.getenv('MY_EMAIL2')],
                         msg=f'{subject}\n\n{message}')
    except (smtplib.SMTPException, OSError, socket.error) as e:
      print(f'{time_now} [ERROR] We have an error: {e}')
    except Exception as e:
      print(f'{time_now} [ERROR] Something other went wrong: {e}')
    else:
      print(f'[INFO]Email sended !')

  def send_sms(self,msg: str)->None:
    """sending  sms"""
    client = Client(os.getenv('ACC_SID'), os.getenv('AH_TOK'))
    message = client.messages.create(
      messaging_service_sid=os.getenv('MSG_SRV_SID'),
      body=msg,
      to=os.getenv('PHONE')
    )

  def send_whatsup_msg(self,event: str,time: str):
    """sending whatsup message"""
    client = Client(os.getenv('ACC_SID'), os.getenv('AH_TOK'))
    message = client.messages.create(
      from_='whatsapp:+14155238886',
      content_sid=os.getenv('CONTENT_SID'),
      content_variables='{"1":"%s","2":"%s"}' % (event, time),
      to=os.getenv('TO'),
    )

