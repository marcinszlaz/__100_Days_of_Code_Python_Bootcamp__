from instafollower import InstaFollower
from dotenv import load_dotenv
import os, pathlib

dotenv_path = pathlib.Path.cwd() / ".env"
load_dotenv(dotenv_path=dotenv_path)

action = InstaFollower()
action.login()
action.follow()
# TODO dodaj 2 nowe funkcje, rozbij przesuwanie
# TODO i klikanie na dwie osobne, tak będzie przeżyściej, potem połącz
# TODO w jedną find_followers()
# action.find_followers()

_input_ = input('give me some input (end of main)')
