from flask import Flask, render_template
import os,pathlib
from dotenv import load_dotenv

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)

@app.route('/')
def main_page():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True,host=f"{os.getenv("HOST_IP")}",port=80)