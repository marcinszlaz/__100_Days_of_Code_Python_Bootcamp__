import datetime as dt
from datetime import date as d
import requests

AGE_URL = "https://api.agify.io/"
GEN_URL = "https://api.genderize.io/"
name = "marcin"

year = d.today()
print(year.year)

headers = \
  { "Accept-Language": "pl-PL;q=1.0,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
  }
age_response = requests.get(url=f"{AGE_URL+'?name='+name}",headers=headers)
gender_response = requests.get(url=f"{GEN_URL+'?name='+name}",headers=headers)


print(age_response.json()["age"])
print(gender_response.json()["gender"])
# print(age_response)



