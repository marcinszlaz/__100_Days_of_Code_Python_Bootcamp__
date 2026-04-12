# project 51

from internetspeedtwitterbot import InternetSpeedTwitterBot
import os, pathlib
from dotenv import load_dotenv

# load variables
auth_path = pathlib.Path.cwd() / ".env"
load_dotenv(dotenv_path=auth_path)
USER_DATA_DIRECTORY = pathlib.Path.cwd() / os.getenv("CHROME_DRIVER_PATH")

print(auth_path)
print(USER_DATA_DIRECTORY)
print(os.getenv("CHROME_DRIVER_PATH"))

action = InternetSpeedTwitterBot()
action.get_internet_speed()
action.tweet_at_provider()

_input_ = input('Give me The Disc !')

