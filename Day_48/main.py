# TODO -> fetch name, price and status of upgrades
# TODO -> check is upgrade available

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import random as r, time as t
from selenium.webdriver.common.keys import Keys # you can use keys on www with this black magic library

COOKIE_URL="https://ozh.github.io/cookieclicker/"
c_count = 0
c_per_sec = 0

# chrome doesn't close immediately with this option
chrome_options: Options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
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
    print(f'Houston, we have a problem {ex}')

# cookie clicker
def cookie_clicker():
  t.sleep(r.uniform(1.5,2.5))
  again = 0
  while again < 10:
    big_cookie = driver.find_element(By.ID,value="bigCookie")
    big_cookie.click()
    t.sleep((round(r.uniform(0.085,0.100),3)))
    again+=1



cookie_consent()
choose_language_EN()
cookie_consent()
cookie_clicker()
cookies_counter()
print('count',c_count,'per sec',c_per_sec)

t.sleep(1)
# driver.quit()
