#Python interpreter treats folder with __init__.py file as a package
#it's better to think about app folder as namespace not file with class/methods
#and that's why you can import files from folder like class/methods
#from ordinary files which have extension *.py

from flask import Flask

app = Flask(__name__)

from app import routes #here you import file routes from namespace(folder)app

