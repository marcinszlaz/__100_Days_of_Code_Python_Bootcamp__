from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os,pathlib
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import random as r, time as t
from selenium.webdriver.common.keys import Keys # you can use keys on www with this black magic library

GYM_URL="https://appbrewery.github.io/gym/"

# path to web browser user profile
user_data_dir1 = os.path.join(os.getcwd(),"chrome_profile")
user_data_dir = pathlib.Path.cwd() / "chrome_profile"

# login and password from .env
auth_path = pathlib.Path.cwd() / ".env"
load_dotenv(dotenv_path=auth_path)

# chrome doesn't close immediately with this option
chrome_options: Options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--start-maximized") # web browser full screen mode
# instead of this above better use driver.maximize_window()

driver: WebDriver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)
t.sleep(r.uniform(0.15,0.25))
# driver.maximize_window() # instead of line 24, line 23 and 24 are conflicted

def login():
  login_button = driver.find_element(By.ID,value="login-button")
  login_button.click()
  t.sleep(r.uniform(0.15,0.25))
  print('login button clicked')
  email_input = driver.find_element(By.ID, value="email-input")
  email_input.send_keys(os.getenv(key="ACCOUNT_EMAIL"))
  t.sleep(r.uniform(0.15,0.25))
  password_input = driver.find_element(By.ID, value="password-input")
  password_input.send_keys(os.getenv(key="ACCOUNT_PASSWORD"))
  t.sleep(r.uniform(0.15,0.25))
  print('credentials typed')
  submit_button = driver.find_element(By.ID, value="submit-button")
  submit_button.click()
  print('logged in')

login()