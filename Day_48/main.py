# TODO -> fetch name, price and status of upgrades
# TODO -> check is upgrade available

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import random as r, time as t, pathlib
from selenium.webdriver.common.keys import Keys # you can use keys on www with this black magic library

COOKIE_URL="https://ozh.github.io/cookieclicker/"
user_data_dir = pathlib.Path.cwd() / "chrome_profile"
c_count = 0
c_per_sec = 0

# chrome doesn't close immediately with this option
chrome_options: Options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
# chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--start-maximized")

driver: WebDriver = webdriver.Chrome(options=chrome_options)
driver.get(COOKIE_URL)

#cookies consent
def cookie_consent():
  t.sleep(r.uniform(1.5,2.5))
  cookie = driver.find_element(By.LINK_TEXT,value="Got it!")
  cookie.click()

# language select
def choose_language_PL():
  t.sleep(r.uniform(1.5,2.5))
  language = driver.find_element(By.ID,value="langSelect-PL")
  language.click()

def choose_language_EN():
  t.sleep(r.uniform(1.5,2.5))
  language = driver.find_element(By.ID,value="langSelect-EN")
  language.click()

def cookies_ps():
  t.sleep(r.uniform(1.5,2.5))
  cps = driver.find_element(By.ID,value="cookiesPerSecond")
  print(cps.text)

def cookies_counter():
  global c_count,c_per_sec
  t.sleep(r.uniform(1.5,2))
  try:
    c_con = driver.find_element(By.CSS_SELECTOR,value="div#cookies")
    c_count = (c_con.text.split()[0])
    c_per_sec = (c_con.text.split()[4])
  except Exception as ex:
    print(f'[ERROR] with `cookies_counter()` {ex}')

# cookie clicker
def cookie_clicker():
  global c_count, c_per_sec
  t.sleep(r.uniform(1.5,2.5))
  five_min_later = t.time() + 60
  five_sec_later = t.time() + 5
  big_cookie = driver.find_element(By.ID,value="bigCookie")
  while t.time() < five_min_later:
    if t.time() < five_sec_later:
      big_cookie.click()
      t.sleep((round(r.uniform(0.045,0.055),3)))
    else:
      print('check shop')
      srch_avail_upgr()
      five_sec_later = t.time() + 5

# upgrades
def srch_avail_upgr():
  """ seeking for available upgrades"""
  upgrades = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
  upgrade = None
  for upg in reversed(upgrades):
    if "enabled" in upg.get_attribute("class"):
      upgrade = upg
      break
  if upgrade:
    upgrade.click()

cookie_consent()
choose_language_EN()
cookie_consent()
cookie_clicker()
t.sleep(1)

# def tryandtry():
#   try:
#     cookie_consent()
#     choose_language_EN()
#     cookie_consent()
#     cookie_clicker()
#     t.sleep(1)
#   except Exception as ex:
#     print('something went terribly wrong')
#   else:
#     tryandtry()

  # try:
  #   cookie_consent()
  #   choose_language_EN()
  #   cookie_consent()
  #   cookie_clicker()
  #   t.sleep(1)
  # except Exception as ex:
  #   print('something went terribly wrong')

# driver.quit()

