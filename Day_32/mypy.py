import smtplib
from dotenv import load_dotenv
import os

# load_dotenv()
# # you can use trick with ... as connection, then you dont have to use connection.close() (like with open(file)
# connection = smtplib.SMTP(host='smtp.gmail.com',port=587) # smtp configuration
# connection.starttls() # enable tls
# connection.login(user=os.getenv('MY_EMAIL'), password=os.getenv('MY_PASS'))
# connection.sendmail(from_addr=os.getenv('MY_EMAIL'), to_addrs=os.getenv('MY_EMAIL2'),msg='Subject:Hello !\n\n Jak tam :)')
# # in this lib (smtplib) you need to use Subject:....\n\n to make title for your mail, it is, hmm, standard
# # if you want something more sophisticated you have to import this `from email.message import EmailMessage`
# connection.close()

# print(f'{os.getenv('MY_PASS')} {os.getenv('MY_EMAIL2')}')

import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))
year = now.year
print(year)
print(type(year))
day_of_week = now.weekday()
print(day_of_week)

day_of_birth = dt.datetime(year=2000, month=1, day=1)
print(day_of_birth)