# project 51

from constants import *
from internetspeedtwitterbot import InternetSpeedTwitterBot
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os, pathlib
from dotenv import load_dotenv
from selenium.webdriver.common.by import By # remove after OOP
from selenium.webdriver.support import expected_conditions as ec # remove after OOP
import random as r, time as t # remove after OOP
from selenium.webdriver.support.wait import WebDriverWait # remove after OPP
from selenium.common.exceptions import TimeoutException # remove after OOP
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc # remove after OOP

# load variables
auth_path = pathlib.Path.cwd() / ".env"
load_dotenv(dotenv_path=auth_path)
USER_DATA_DIRECTORY = pathlib.Path.cwd() / os.getenv("CHROME_DRIVER_PATH")

"""
# chrome doesn't close immediately with this option
chrome_spd_test: Options = webdriver.ChromeOptions()
chrome_spd_test.add_experimental_option("detach",True)
chrome_spd_test.add_argument(f"--user-data-dir={USER_DATA_DIRECTORY}")
chrome_spd_test.add_argument(f"--profile-directory={CHROME_PROFILE}")

driver: WebDriver = webdriver.Chrome(options=chrome_spd_test)
driver.maximize_window()
driver.get(SPEED_TEST_URL)
print(driver.title)
wait = WebDriverWait(driver, 5)
"""
"""
# driver for speed test www
# chrome STEALTH MODE xD
options_spd_test = uc.ChromeOptions()
options_spd_test.add_argument(f"--user-data-dir={os.getenv("CHROME_DRIVER_PATH")}")
# options_spd_test.add_argument(f"--profile-directory={CHROME_PROFILE}")
# options_spd_test.add_argument("--disable-extensions")
# options_spd_test.add_argument("--no-first-run")
# options_spd_test.add_argument("--no-default-browser-check")
# options_spd_test.add_argument("--disable-popup-blocking")
driver_spd_test = uc.Chrome(options=options_spd_test, use_subprocess=True)
# uc.Chrome(options=options_spd_test, use_subprocess=True)
driver_spd_test.maximize_window()
driver_spd_test.get(SPEED_TEST_URL)
wait_spd_test = WebDriverWait(driver_spd_test, 20)
"""
#driver for twitter www
# options_twitter = uc.ChromeOptions()
# options_twitter.add_argument(f"--user-data-dir={USER_DATA_DIRECTORY}")
# options_twitter.add_argument(f'--profile-directory={CHROME_PROFILE}')
# driver_twitter = uc.Chrome(options=options_twitter)
# driver_twitter.maximize_window()
# driver_twitter.get(TWITTER_URL)
# wait_twitter = WebDriverWait(driver_twitter, 3)


# action = InternetSpeedTwitterBot()
# action.get_internet_speed()

_input_ = input('Give me The Disc !')

