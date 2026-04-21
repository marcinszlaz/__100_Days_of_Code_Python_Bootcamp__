import random as r
from flask import Flask
import pathlib,os
from dotenv import load_dotenv

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)

correct='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'
high='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
low='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
numbers='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'

app = Flask(__name__) # constructor Flask class require import name
@app.route('/')
def display_greetings():
  return (f'<h1 style="color: teal">Guess a number between 0 and 9</h1>'
          f'<br />'
          f'<img type="gif" src="{numbers}">')

def random_number_generator():
  rm = r.randint(0,9)
  print(f'lucky number is: ', rm)
  return rm
guessed_number = random_number_generator()

@app.route('/<int:number>')
def guess_the_number(number):
  if number == guessed_number:
    return (f'<h1 style="color: green">You found me!</h1>'
            f'<br />'
            f'<img type="gif" src="{correct}">')
  elif number > guessed_number:
    return (f'<h1 style="color: purple">Too high, try again!</h1>'
            f'<br />'
            f'<img type="gif" src="{high}">')
  else:
    return (f'<h1 style="color: red">Too low, try again!</h1>'
            f'<br />'
            f'<img type="gif" src="{low}">')



if __name__ == "__main__":

  app.run(host=f"{os.getenv("HOST_IP")}",port=80,debug=True)