from flask import Flask, render_template,request
import os,pathlib
from dotenv import load_dotenv
from markupsafe import escape

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)

app=Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login',methods=['GET','POST']) # magic route has methods parameter xD
def receive_data():
  header = request.headers
  method = request.method
  login = request.form['user_login']
  password = request.form['user_password']
  args = request.args
  return (f"used method: {method}<br>"
          f"args: {args.values()}<br>"
          f"<h1>Hello {escape(login)} it seems your password is ` {escape(password)} ` </h1>"
          f"")
# without escape() you are vulnerable to scripts attacks,
# for example user type login = <script>alert("boom!")</script>
# and your screen will blow up ;)

if __name__=="__main__":
  app.run(debug=True, host=f"{os.getenv("HOST_IP")}", port=80)
