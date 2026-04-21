# for render_template() purpose you have create template folder
# for index.html and static folder and inside it css/image and other folders
# for css files and photos, css/image folders aren't obligatory, but it is
# good practice and general cleanup

from flask import Flask, render_template
from dotenv import load_dotenv
import pathlib,os

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)
@app.route('/')
def home_page():
  return render_template("index.html")


if __name__ == "__main__":
  app.run(port=80,host=f"{os.getenv("HOST_IP")}",debug=True)
