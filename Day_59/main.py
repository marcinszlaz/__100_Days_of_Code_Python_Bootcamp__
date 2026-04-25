from flask import Flask, render_template
import requests
from datetime import datetime as dt

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

@app.route('/contact')
def contact():
  global year
  return render_template('contact.html',year=year)

@app.route('/post/<int:post_id>')
def display_post(post_id):
  global blogs
  return render_template('post.html',post_id=post_id,blogs=blogs)

if __name__ == "__main__":
  app.run(debug=True,host="10.215.14.2",port=80)
