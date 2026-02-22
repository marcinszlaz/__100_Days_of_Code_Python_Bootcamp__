import datetime as dt
import os,dotenv

dotenv.load_dotenv()
time = dt.datetime.now().strftime('%H:%M:%S')
tajm = dt.datetime.now()
print(time, tajm)
print(os.environ)
print(type(os.environ))
for (key,value) in os.environ.items():
  print('klucz:',key,'wartosc:',value)
