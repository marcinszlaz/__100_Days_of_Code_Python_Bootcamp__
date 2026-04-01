from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os,pathlib
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import random as r, time as t
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys # you can use keys on www with this black magic library

GYM_URL="https://appbrewery.github.io/gym/"

# path to web browser user profile
user_data_dir1 = os.path.join(os.getcwd(),"chrome_profile")
user_data_dir = pathlib.Path.cwd() / "chrome_profile" # new, better way
# with overloaded operator of concatenation `/`

# login and password from .env, it isn't necessary but hey, good practice bro :)
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
# driver.implicitly_wait(0) # it is global setting for web driver, not good, 0 is default
wait = WebDriverWait(driver, 2) # it's better way than driver.implicitly_wait(float) because it has extended conditions to use, and you can customize time for each instance of button, input,etc.
# t.sleep(r.uniform(0.15,0.25))
# driver.maximize_window() # instead of line 24, line 23 and 24 are conflicted

def login():
  # driver.implicitly_wait(2)
  # login_button = driver.find_element(By.ID,value="login-button")
  login_button = wait.until(ec.element_to_be_clickable((By.ID,"login-button")))
  login_button.click()
  # t.sleep(r.uniform(0.15,0.25))
  print('login button clicked')
  # email_input = driver.find_element(By.ID, value="email-input")
  email_input = wait.until(ec.presence_of_element_located((By.ID,"email-input")))
  email_input.clear() #it is important, clear typing area before type new content
  email_input.send_keys(os.getenv(key="ACCOUNT_EMAIL"))
  # t.sleep(r.uniform(0.15,0.25))
  # password_input = driver.find_element(By.ID, value="password-input")
  password_input = wait.until(ec.presence_of_element_located((By.ID,"password-input")))
  password_input.clear()
  password_input.send_keys(os.getenv(key="ACCOUNT_PASSWORD"))
  # t.sleep(r.uniform(0.15,0.25))
  print('credentials typed')
  # submit_button = driver.find_element(By.ID, value="submit-button")
  submit_button = wait.until(ec.element_to_be_clickable((By.ID,"submit-button")))
  submit_button.click()
  print('Am I logged? :',amilogged())

def amilogged():
  # driver.implicitly_wait(2)
  # t.sleep(r.uniform(0.15,0.25))
  # schedule_page = driver.find_element(By.ID, value="schedule-page")
  schedule_page = wait.until(ec.presence_of_element_located((By.ID,"schedule-page")))
  if not schedule_page:
    return False
  else:
    return True

def schedule():
  schedule_plan = wait.until(ec.presence_of_element_located((By.ID,"schedule-page")))
  plan_blocks = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'div[id^="day-group-"]')))


# core xD
login()
# driver.implicitly_wait(0)
