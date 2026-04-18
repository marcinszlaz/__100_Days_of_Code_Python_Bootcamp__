import requests,os,pathlib
from constans import *
from dotenv import load_dotenv
import pprint as pp
import time as t, random as r
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, SessionNotCreatedException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

dotenv_path = pathlib.Path.cwd() / ".env"
load_dotenv(dotenv_path=dotenv_path)

header = \
  { "Accept-Language": "pl-PL;q=1.0,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
  }
response = requests.get(url=ZILLOW_URL, headers=header)
print('Status code: ',response.status_code)
print('Errors: ',response.raise_for_status())
t.sleep(1)
soup: BeautifulSoup = BeautifulSoup(markup=response.text, features="html.parser")

#fetching anchors
find_all_anchors = soup.find_all(name="a",attrs={"class": "property-card-link"})
anchor_list = [a["href"] for a in find_all_anchors]
select_anchors = soup.select('a[class="property-card-link"]')
anchor_list_ = [a["href"] for a in select_anchors]

# fetching prices list
prices = soup.select('span[data-test^="property-card-price"]')
prices_list = [_.text for _ in prices]

# fetching addresses list
addresses = soup.select('address[data-test^="property-card"]')
addresses_list = [_.text for _ in addresses]

def are_lists_equal(list_1: list, list_2: list)->None:
  """checks equality of lists length and compares their content equality
  function handles with only two lists"""
  merged_list = [_ for _ in zip(list_1, list_2)]
  if len(list_1) != len(list_2):
    print('Lists length arent equal')
  else:
    print('Lists length are equal')
    i = 0
    for _ in merged_list:
      i += 1
      if _[0] == _[1]:
        print(f'indexes: {i} are EQUAL')
      elif _[0] != _[1]:
        print(f'indexes: {i} are NOT EQUAL')
      else:
        print(f'url_list length: {len(list_1)} url_list_ length: {len(list_2)}')

def human_click(element):
  """ standard Selenium .click() always point at x=0,y=0
  middle of the button  """
  global driver
  # fetching button size
  width = element.size['width']
  height = element.size['height']
  # randomize offset, 20-70% of button size
  offset_x = r.randint(int(width * 0.2), int(width * 0.7)) - (width / 2)
  offset_y = r.randint(int(height * 0.2), int(height * 0.7)) - (height / 2)
  # make a move !
  action = ActionChains(driver)
  action.move_to_element_with_offset(element, offset_x, offset_y)
  action.click()
  action.perform()
  print(f"Button hit at: {offset_x}, {offset_y}")

def rand_time():
  x = r.uniform(1,1.3)
  y = r.uniform(1.8,2.3)
  return t.sleep(r.uniform(a=x, b=y))

cleared_prices = []
def clear_prices(list_: list,print_=False)->list:
  for _ in list_:
    cleared_prices.append(_.replace(' ','').replace('+','').replace('/mo','').replace('1bd',''))
  if print_ == True:
    pp.pprint(cleared_prices)
  return cleared_prices

cleared_addresses = []
def clear_addresses(list_: list,print_ = False)->list:
  for _ in list_:
    cleared_addresses.append((_.strip().replace('|','')))
  if print_ == True:
    pp.pprint(cleared_addresses,width=120)
  return cleared_addresses

# driver section
driver,wait = None,None
try:
  options = uc.ChromeOptions()
  options.add_argument(f"--user-data-dir={os.getenv("CHROME_PATH")}")
  # options.add_argument('--lang=en-US')
  driver = uc.Chrome(options=options, use_subprocess=True, version_main=147)
  version = uc.Patcher()
  print('Webdriver version: ',version)
except (SessionNotCreatedException, TimeoutException, Exception) as er:
  print(f'[ERROR] driver doesn\'t run! {repr(er)}\n{er}')
else:
  driver.get(RESPONDENT_LINK)
  driver.maximize_window()
  wait = WebDriverWait(driver, 10)
t.sleep(1)
# check lists length
if len(anchor_list_) == len(prices_list) and len(addresses_list) == len(prices_list):
  print('Lists length are equal')
# clear data
clear_addresses(addresses_list)
clear_prices(prices_list)

# filling data in form
# x = len(prices_list)
# for _ in range(x):
for _ in range(5):
  try:
    property_address_input = wait.until(ec.presence_of_element_located((By.XPATH, '(//input[@type="text"])[1]')))
    property_address_input.send_keys(cleared_addresses[_])
    rand_time()
    price_per_month_input = wait.until(ec.presence_of_element_located((By.XPATH, '(//input[@type="text"])[2]')))
    price_per_month_input.send_keys(cleared_prices[_])
    rand_time()
    property_link_input = wait.until(ec.presence_of_element_located((By.XPATH, '(//input[@type="text"])[3]')))
    property_link_input.send_keys(anchor_list_[_])
    rand_time()
    submit_button = wait.until(ec.presence_of_element_located((By.XPATH, '(//div[@role="button"]/div)[2]')))
    human_click(submit_button)
    rand_time()
    send_next = wait.until(ec.presence_of_element_located((By.XPATH,'//a[contains(@href,"confirm")]')))
    human_click(send_next)
    rand_time()
  except (TimeoutException, Exception) as er:
    print(f'[ERROR] we got an error, you probably aren\'t login (google account)\
          or button are non clickable xD {repr(er)}\n{er}')

driver.refresh()
input('Data sended to forms (hit any key to quit)')
