from instafollower import InstaFollower
from dotenv import load_dotenv
import pathlib

dotenv_path = pathlib.Path.cwd() / ".env"
load_dotenv(dotenv_path=dotenv_path)

action = InstaFollower()
action.login()
action.follow()
action.find_followers()

tactical_debugging_input = input('Give me some input (end of main)')
