# document.body.contentEditable - browser/F12, you can edit content
# but only until browser refresh :)

from flask import Flask, render_template
from dotenv import load_dotenv
import pathlib,os

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)
@app.route('/')
def home_page():
  # return f"<h1>Hello World</h1>"
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True,host=f"{os.getenv("HOST_IP")}",port=80)