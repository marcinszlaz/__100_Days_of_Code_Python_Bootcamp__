from flask import Flask, render_template
import requests
from datetime import datetime as dt
import os,pathlib
from dotenv import load_dotenv
from markupsafe import escape
from flask import request
import smtplib as sm
from notification_manager import NotificationManager as nm

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)
nm = nm()

# year
year = dt.now().year

# `fetching api data section`
url = 'https://api.npoint.io/5e3fb42bf9c2977b93fe'
headers = {
    "Accept-Language": "pl-PL;q=1.0,pl;q=0.9,en-US;q=0.8,en;q=0.7",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
response = requests.get(url=url,headers=headers)
blogs = response.json()

#sending mail
def send_email(msg: str):
  recipent = f"{os.getenv('MY_EMAIL')}"
  message = f"""Subject: Marcin\'s Blog\n\n{msg}""".encode("UTF-8")
  with sm.SMTP(host=os.getenv("SMTP"), port=os.getenv("MY_PORT") ) as conn:
    conn.starttls()
    conn.login(user=os.getenv('MY_EMAIL'),password=os.getenv('MY_PASSWORD'))
    conn.sendmail(from_addr=recipent,to_addrs=recipent,msg=message)


# `server section ;)`
app = Flask(__name__)
@app.route('/')
def main_page():
  global blogs,year
  return render_template('index.html',blogs=blogs,year=year)

@app.route('/about')
def about():
  global year
  return render_template('about.html',year=year)

@app.route('/contact', methods=["POST","GET"])
def contact():
  global year
  contact = "Contact Me!"
  if request.method == 'GET':
    return render_template('contact.html',year=year,contact=contact)
  elif request.method == 'POST':
    contact="Message has been sent successful"
    userName = request.form['userName']
    userEmail = request.form['userEmail']
    userPhone = request.form['userPhone']
    userMessage = request.form['userMessage']
    nm.send_email(subject=f"Marcin's Blog", message = userMessage)
    send_email(userMessage)
    return render_template('contact.html', userName=userName, userEmail=userEmail, userPhone=userPhone, userMessage=userMessage, year=year, contact=contact)

@app.route('/post/<int:post_id>')
def display_post(post_id):
  global blogs,year
  return render_template('post.html',post_id=post_id,blogs=blogs,year=year)

@app.route('/form-entry',methods=["POST","GET"]) # obsolete artifact, but I don't have heart to cut it out xD
def receive_data():
  global year
  if request.method == 'POST':
    userName = request.form['userName']
    userEmail = request.form['userEmail']
    userPhone = request.form['userPhone']
    userMessage = request.form['userMessage']
    return render_template('message-sent.html',userName=userName,userEmail=userEmail,userPhone=userPhone,userMessage=userMessage,year=year)
  elif request.method == 'GET':
    return render_template('message-sent.html')

if __name__ == "__main__":
  app.run(debug=True,host=f"{os.getenv('HOST_IP')}",port=f"{os.getenv('HOST_PORT')}")
