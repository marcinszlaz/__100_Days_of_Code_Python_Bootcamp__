# FILE NAMES = {"static": 'static', "templates": 'templates}
import datetime as dt
from flask import Flask, render_template
from datetime import date as d
import requests
import os,pathlib
from dotenv import load_dotenv

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)

AGE_URL = "https://api.agify.io/"
GEN_URL = "https://api.genderize.io/"
BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"
year = d.today().year
# year = dt.datetime.now().year

# main page
app=Flask(__name__)
@app.route('/')
def home_page():
  global year
  return render_template("index.html",year=year)

# guessing page
@app.route('/guess/<string:name>')
def guess_age_sex(name):
  global year
  headers = \
  { "Accept-Language": "pl-PL;q=1.0,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
  }
  age_response = requests.get(url=f"{AGE_URL+'?name='+name}",headers=headers)
  gender_response = requests.get(url=f"{GEN_URL+'?name='+name}",headers=headers)
  age = age_response.json()["age"]
  gender = gender_response.json()["gender"]
  return render_template("guess.html",name=name,age=age,gender=gender,year=year)

#page with blog
@app.route('/blog/<num>')
def get_blog(num):
  global year
  headers = \
    {"Accept-Language": "pl-PL;q=1.0,pl;q=0.9,en-US;q=0.8,en;q=0.7",
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
     }
  blog_response = requests.get(url=BLOG_URL,headers=headers)
  blog = blog_response.json()
  return render_template("blog.html", year=year, posts=blog)

if __name__ == "__main__":
  app.run(debug=True,host=f"{os.getenv("HOST_IP")}",port=80)
