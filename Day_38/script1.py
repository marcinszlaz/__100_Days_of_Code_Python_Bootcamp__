"""
Character limit: Maximum 50 characters
Supported activities:
Running/Jogging - "ran for 30 minutes", "jogged 2 miles"
Swimming - "swam for 1 hour", "swimming laps"
Walking - "walked 3 miles", "brisk walk 45 min"
Cycling - "biked for 1 hour", "rode bike 10 miles"
Weightlifting - "lifted weights 45 min", "weight training"
Tip: Include duration (e.g., "30 min", "1 hour") for accurate calorie estimates.
Authorization: Basic bnVsbDpudWxs <---> basic auth on sheet's site, encode64
"""


# import logging
# import http.client as http_client
# http_client.HTTPConnection.debuglevel = 1

import requests
import pathlib,os
from dotenv import load_dotenv
import datetime as dt

# VARIABLES
BASE_URL="https://app.100daysofpython.dev"
POST= "v1/nutrition/natural/exercise"

# GETTING .ENV
path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=path)

# FETCHING EXERCISES, DURATION AND CALORIES
headers = {
"x-app-id":os.getenv('APP_ID'),
"x-app-key":os.getenv('API_KEY'),
"Content-Type": "application/json",
}
exercise_text = input("Tell me which exercise you did ?")
data = {
  "query": exercise_text,
  "weight_kg": 100,                  # Optional: Weight in kg (1-500)
  "height_cm": 196,                 # Optional: Height in cm (1-300)
  "age": 42,                        # Optional: Age (1-150)
  "gender": "male"                  # Optional: "male" or "female"
}
response = requests.post(url=f"{BASE_URL}/{POST}", json=data, headers=headers)
exercises_data = response.json()
print(exercises_data)
print(exercises_data['exercises'][0]['name'],exercises_data['exercises'][0]['duration_min'],exercises_data['exercises'][0]['nf_calories'])

# POSTING DATA ON GOOGLE SPREADSHEET (api.sheety.co)
today = dt.datetime.now().strftime('%d/%m/%Y')
time = dt.datetime.now().strftime('%H:%M:%S')
exercise = exercises_data['exercises'][0]['name']
duration = exercises_data['exercises'][0]['duration_min']
calories = exercises_data['exercises'][0]['nf_calories']

headers = {
  "Content-type":"application/json",
  "Authorization": "Basic bnVsbDpudWxs"
}

workout = {
  "workout": {
      "date": today,
      "time": time,
      "exercise": exercise,
      "duration": duration,
      "calories": calories,

  }
}
response = requests.post(url=os.getenv('SHEET_URL'), headers=headers, json=workout, auth=(os.getenv('AUTH_LOGIN'),os.getenv('AUTH_PASS')))
print(response.text)
response = requests.get(url=os.getenv('SHEET_URL'), headers=headers)

# DELETE ROW xD this doesn't work at all :)
# response1 = requests.delete(url=f'{os.getenv('SHEET_URL')}/4', headers=headers)
# UPDATE ROW xD this doesn't work at all too and it's fine ;]
# response1 = requests.put(url=f'{os.getenv('SHEET_URL')}/4', headers=headers)
