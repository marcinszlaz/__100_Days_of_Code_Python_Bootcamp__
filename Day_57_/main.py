from flask import Flask, render_template
import requests

# requests block
post_url ="https://api.npoint.io/c790b4d5cab58020d391"
headers = \
    {
    "Accept-Language": "pl-PL;q=1.0,pl;q=0.9,en-US;q=0.8,en;q=0.7",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }
response = requests.get(url=post_url,headers=headers)
blogs = response.json()

app = Flask(__name__)
@app.route('/')
def home():
    global blogs
    return render_template("index.html",response_ = blogs)

@app.route('/post/<int:post_id>') # post_id - same var name
def display_blog(post_id):        # post_id - its obligatory
    global blogs
    return render_template("post.html",any_key=post_id,blogs_ = blogs)
    # here you can have anything = post_id but post_id have to post_id

if __name__ == "__main__":
    app.run(debug=True, host="10.215.14.2",port=80)
