# I can't finish the project, tinder account was blocked xD
# because I'm the filthy bot

from selenium.webdriver.chrome.webdriver import WebDriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os, pathlib
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import random as r, time as t
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

TINDER_URL="https://tinder.com/"
user_data_directory = pathlib.Path.cwd() / "chrome_profile"

one = '//*[@id="s1497981041"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[1]'
two = '//*[@id="s1497981041"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[1]/div'
three ='//*[@id="s13228980"]'
three_cs ="" # later check CSS selector, I think it isn't work properly
four = '//*[@id="s13228980"]/div'
five = '//*[@id="gsi_317059_895374"]'
one_to_five_dict = {1:one,2:two,3:three,4:four,5:five}

auth_path = pathlib.Path.cwd() / ".env"
load_dotenv(dotenv_path=auth_path)

"""
# chrome doesn't close immediately with this option
chrome_options: Options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument(f"--user-data-dir={user_data_directory}")

driver: WebDriver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(TINDER_URL)
wait = WebDriverWait(driver, 3)
"""

# chrome STEALTH MODE xD
options = uc.ChromeOptions()
# options.add_experimental_option("detach",True)
options.add_argument(f"--user-data-dir={user_data_directory}")

driver = uc.Chrome(options=options)
driver.maximize_window()
driver.get(TINDER_URL)
wait = WebDriverWait(driver, 3)

#cookie disagree
def cookie_not():
  terms_disagree_button  = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'div div[class="My(8px)"]:nth-child(2) button:first-child')))
  terms_disagree_button.click()

#cookie consent
def cookie_yes():
  try:
    terms_agree_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'div div[class="My(8px)"] button:first-child')))
  except TimeoutException as tx:
    print("Cookie agreement probably done during previous run")
  else:
    terms_agree_button.click()

# too many complication xD, I can login, but 2FA is killing my bot xD
# we have to try use fb
def login_by_google():
  try:
    login_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'div[class^="Mx(12px)"]:nth-child(2) div[class*="lxn9"]')))
  except ValueError as ev:
    print('Something unsurprisingly blew up :)')
  else:
    login_button.click()

  try:
    login_continue = wait.until(ec.presence_of_element_located((By.XPATH,three)))
  except ValueError as ev:
    print(f'[ERROR] Cannot login, see screen {ev}')
    driver.save_screenshot("./screenshoots/screen.png")
  else:
    login_continue.click()

  # save current window id, all windows id and focus on last opened window
  original_window = driver.current_window_handle
  all_windows = driver.window_handles
  driver.switch_to.window(all_windows[-1])

  try:
    input_email = wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="identifierId"]')))
  except ValueError as ev:
    print(f'[ERROR]{ev}')
  else:
    t.sleep(r.uniform(3,6))
    input_email.send_keys(os.getenv("TINDER_LOGIN"))
    t.sleep(r.uniform(0.3,1))
    next_button = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="identifierNext"]/div/button/span')))
    next_button.click()

  try:
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    input_password = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
  except ValueError as ev:
    print(f'[ERROR] {ev}')
  else:
    t.sleep(r.uniform(3,5))
    input_password.send_keys(os.getenv("TINDER_PASSWORD"))
    t.sleep(r.uniform(0.3,1))
    input_password.send_keys(Keys.ENTER)
    # '//*[@id="passwordNext"]/div/button/div[3]'
    # next_button = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="passwordNext"]/div/button/div[3]')))
    # next_button.click()


cookie_yes()
login_by_google()

_input_ = input("Input size of your penis :] ")

