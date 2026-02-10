##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import os
from dotenv import load_dotenv
import smtplib as sm

load_dotenv()
df = pd.read_csv(filepath_or_buffer='birthdays.csv')
letters_list = ['letter_1.txt','letter_2.txt','letter_3.txt']

def send_email(recipent=f'{os.getenv('MY_EMAIL2')}',message='Subject:Hello\n\nHello'):
  with sm.SMTP(host=os.getenv('MY_HOST'),port=os.getenv('MY_PORT')) as conn:
    conn.starttls()
    conn.login(user=os.getenv('MY_EMAIL'),password=os.getenv('MY_PASSWORD'))
    conn.sendmail(from_addr=os.getenv('MY_EMAIL'),to_addrs=recipent,msg=message)
    # conn.close() you don't have to with with :)

def letter_lottery(chosen_letter, chosen_one):
  random_letter = random.choice(chosen_letter)
  with open(file=f'letter_templates/{random_letter}', mode='r') as file:
    letter = file.read().replace('[NAME]',chosen_one)
  return letter

# wyłuskanie dat z csv
month = dt.datetime.now().month
day = dt.datetime.now().day
for row in df[['year','month','day','name','email']].itertuples():
  birthday = '{2!s}/{1!s}/{0!s}'.format(row.year,row.month, row.day)
  birthday_person = row.name
  bp_email = row.email
  date_diff = dt.datetime.strptime(birthday,'%d/%m/%Y')
  if date_diff.month == month and date_diff.day == day:
    send_email(recipent=bp_email,message=f'Subject:Happy Birthday !\n\n{letter_lottery(letters_list,birthday_person)}')



# wyłuskanie z pandas, da sie ale nie dostajesz czystej daty tylko panda series, to przy malej ilości danych overkill
date_diff = pd.to_datetime(df[['year','month','day']]) # dla to_datetie dajesz kolumny z datami/data
# print(date_diff)
# print(type(date_diff))
