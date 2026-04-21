# PROJECT 54 :)

# filename cannot have name flask/Flask, you can name it hello, or other
# in terminal (venv) use command
# STEP1) CTRL + ` STEP2) `FLASK --APP <FILE_NAME[WITHOUT.PY]> RUN`
# step1) ctrl + ` step2) `flask --app <file_name[without.py]> run`
# this will run serwer at  http://127.0.0.1:5000 (localhost)
# ctrl + c  - disable running server, it's only test server, not production
# setting variable: unix/linux/git_bash: export FLASK_APP=script1.py
# windows: cmd set FLASK_APP=script1.py / ps $evn:FLASK_APP=script1.py
# po dodaniu zmiennej możesz odpalać `flask run` nie musisz
# podawać flask --app <nazwa> run albo python -m flask --app <nazwa> run
# alternative way is ` if __name__ == "__main__":
#                          app.run() `
# it means if special attribute (__name__) equal __main__ run app.run()
# app.run() means the same as console `flask --app <nazwa> run`

from flask import Flask
import time
import pathlib,os
from dotenv import load_dotenv

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)

print('name of app/file:',__name__)
print('name of other time.__name__',time.__name__)

@app.route("/") # it's decorator, new concept in Python
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/boobs")
def hit_like():
    return "booobs xD"

# this code below ensures you're running current file
if __name__ == "__main__": # it runs application without terminal, using magic `green arrow` :)
    app.run(host=f"{os.getenv("HOST_IP")}") # my ip address in LAN, by default
    # flask run only on localhost, other computers in network can't
    # see www server
