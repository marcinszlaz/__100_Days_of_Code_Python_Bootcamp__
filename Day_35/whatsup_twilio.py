#!/usr/bin/env python3

from twilio.rest import Client
import os
from dotenv import load_dotenv

def send_whatsup_msg(event, time):
  path = os.path.join(os.getcwd(),'.env')
  load_dotenv(dotenv_path=path)
  client = Client(os.getenv('ACC_SID'),os.getenv('AH_TOK'))
  message = client.messages.create(
    from_='whatsapp:+14155238886',
    content_sid=os.getenv('CONTENT_SID'),
    content_variables='{"1":"%s","2":"%s"}' % (event,time),
    to=os.getenv('TO'),
  )

  print(message.sid)
