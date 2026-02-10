import os,dotenv
import smtplib as sm
import random as r
import datetime as dt
import locale # local settings

dotenv.load_dotenv()
quotes_list=[]
# current day
locale.setlocale(locale.LC_ALL,'en_EN.UTF-8') # local settings (pl_PL.UTF-8)
now = dt.datetime.now()
day_name = now.strftime('%A')
print(day_name)

# file quotes to list
with open(file='quotes.txt',mode='r') as file:
  quotes_list=[row.strip() for row in file.readlines()]

print(quotes_list)
print(len(quotes_list))
quote=r.choice(quotes_list)
print(quote)

if dt.datetime.now().weekday()=='1':
  with sm.SMTP(host='smtp.gmail.com',port=587) as conn:
    conn.starttls()
    conn.login(user=os.getenv('MY_EMAIL'),password=os.getenv('MY_PASSWORD'))
    conn.sendmail(from_addr=os.getenv('MY_EMAIL'),to_addrs=os.getenv('MY_EMAIL2'),
                  msg=(f'Subject:Motywacja na poniedzialek xD\n\n{quote}').encode(encoding='utf-8'))
else:
  print(f'Today we have {dt.datetime.now().strftime('%A')} we send monday motivation emails only on Tuesdays '
        f'! xD')