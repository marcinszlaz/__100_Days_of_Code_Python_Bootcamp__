# PROJECT 54 , final project in file server.py
# comments in script1.py

from flask import Flask
import time
import pathlib,os
from dotenv import load_dotenv

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)

print('name of app/file:',__name__)
print('name of other time.__name__',time.__name__)

def bold(arg1):
  def wrapper(*args,**kwargs):
    return f"<b>{arg1()}</b>"
  return wrapper

def underline(arg1):
  def wrapper():
    return f"<u>{arg1()}</u>"
  return wrapper

# something is wrong with this decorator,
# it can't handle with multiple arguments (*args/**kwargs)
# def test_decorator(arg1):
#   def wrapper(*args,**kwargs):
#     return arg1(), args[0],args[1]
#   return wrapper

def italic(arg1):
  def wrapper(*args,**kwargs):
    return f"<i>{arg1()}</i>"
  return wrapper

@app.route("/") # decorator
def hello_world():
    return "<h1>Hello, World!</h1>" # you can send here inline css

@app.route("/boobs")
def display():
    return "booobs xD"

@app.route("/bye")
@underline
@bold
@italic
def display_():
    return "<h1>Bye!</h1>"

@app.route("/username/<name_variable>")
def display_name(name_variable):
  return f"<h1>{name_variable}</h1>"

@app.route("/username_/<path:name_variable>/Italic")
def display_name_(name_variable):
  return f"<em><h2>{name_variable}</h2></em>"

@app.route("/has/<name>/<int:age>")
def has(name,age):
  return f"<h1>{name} has {age} years!</h1>"

if __name__ == "__main__":
    app.run(host=f"{os.getenv("HOST_IP")}", debug=True,port=80)

