from twilio.rest import Client
from dotenv import load_dotenv
import pathlib,os

def send_sms(msg):
  path=pathlib.Path.cwd() / '.env'
  load_dotenv(dotenv_path=path)
  account_sid = os.getenv('ACC_SID')
  auth_token = os.getenv('AH_TOK')
  client = Client(account_sid, auth_token)
  message = client.messages.create(
    messaging_service_sid=os.getenv('MSG_SRV_SID'),
    body=msg,
    to=os.getenv('PHONE')
  )
  # print('message_sid',message.sid)
