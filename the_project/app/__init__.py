#Python interpreter treats folder with __init__.py file as a package
#it's better to think about app folder as namespace not file with class/methods
#and that's why you can import files from folder like class/methods
#from ordinary files which have extension *.py

from flask import Flask
from config import Config #config.py in the_project folder
#from app.config import Config #config.py in app folder
  
app = Flask(__name__)
app.config.from_object(Config)

#it's one way to do this, but we do it different
#app.config['SECRET_KEY'] = 'you-will-never=guess'
# ... add more variables here as needed
  
from app import routes #here you import file routes from namespace(folder)app
#and import is made intentional not below first import but in line 10
#it's about circural imports, this type of imprt helps avoid them

