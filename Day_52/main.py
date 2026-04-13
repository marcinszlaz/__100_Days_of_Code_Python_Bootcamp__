from instafollower import InstaFollower
from dotenv import load_dotenv
import os, pathlib

dotenv_path = pathlib.Path.cwd() / ".env"
load_dotenv(dotenv_path=dotenv_path)

action = InstaFollower()
action.login()
action.follow()

_input_ = input("Give some input !")
