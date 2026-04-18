# You have to make google form yourself, input urls and login/pass
# into .env and constans.py
# program can't login into google account, but it's ok, because project doesn't
# require it

import requests,os,pathlib
from click import argument
from scipy.special.cython_special import rel_entr

from constans import *
from dotenv import load_dotenv
import pprint as pp
import time as t, random as r
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, SessionNotCreatedException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

dotenv_path = pathlib.Path.cwd() / ".env"
load_dotenv(dotenv_path=dotenv_path)

# "Accept-Language": "pl-PL;q=1.0,pl;q=0.9,en-GB,en;q=0.7"
header = \
  { "Accept-Language": "pl-PL;q=1.0,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
  }
response = requests.get(url=ZILLOW_URL, headers=header)
print('Status code: ',response.status_code)
print('Errors: ',response.raise_for_status())
t.sleep(1)
soup: BeautifulSoup = BeautifulSoup(markup=response.text, features="html.parser")

### --------- fetching urls, soup.find_all() way ------ #######
find_all_anchors = soup.find_all(name="a",attrs={"class": "property-card-link"})
anchor_list = [a["href"] for a in find_all_anchors]

### ------- fetching list of url soup.select() way ------- ####
# select_anchors = soup.select('ul[class^="List"] li[class^="ListItem"] a[class^="property-card-link"]') # this version is hardcore, CPU begs for mercy xD, NEVER uncomment this feature xD
select_anchors = soup.select('a[class="property-card-link"]')
anchor_list_ = [a["href"] for a in select_anchors]

# fetching prices list
prices = soup.select('span[data-test^="property-card-price"]')
prices_list = [_.text for _ in prices]

# fetching addresses list
addresses = soup.select('address[data-test^="property-card"]')
addresses_list = [_.text for _ in addresses]

# merged_list = zip(url_list, url_list_) # here you get iterable object
# it's ok but it'll disappear after use, zip object is for disposable use only
def are_lists_equal(list_1: list, list_2: list)->None:
  """checks equality of lists length and compares their content equality
  function handles with only two lists"""
  merged_list = [_ for _ in zip(list_1, list_2)] # we wanna list of tuple
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

def relentless_searcher(object):
  """ Function takes selenium iterable object and return list
  of objects ready to click or enter, you may cal me stupid, why I make my own list ?
   Because after hundreds of errors I don't trust Selenium objects, that is why xD """
  tmp_list = []
  index = 0
  for _ in object:
    index += 1
    tmp_list.append(_)
    print(f'[INFO] obj:{index} {_}')
  return tmp_list

def relentless_clicker(list_,send="xxx"):
  """Click them all!"""
  index = 0
  for _ in list_:
    index += 1
    name = _.tag_name
    # sends click
    try:
      human_click(_)
      rand_time()
      _.send_keys(send)
      print(f'[INFO] Clicked! {index} {name}')
    except (ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException, Exception) as er:
      print(f'[INFO] Can\'t click them! {index}')
    else:
      print(f'[INFO] object: {index} is clickable ')
    # sends Enter
    try:
      _.send_keys(Keys.ENTER)
      rand_time()
      print(f'[INFO] Object {index} {name} Entered!')
    except (ElementClickInterceptedException,StaleElementReferenceException,ElementNotInteractableException, Exception) as er:
      print(f'[INFO] Can\'t use ENTER on object {index} {repr(er)}')
    else:
      print(f'[INFO] object: {index} is enterable ')


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

driver,wait = None,None
try:
  options = uc.ChromeOptions()
  options.add_argument(f"--user-data-dir={os.getenv("CHROME_PATH")}")
  # options.add_argument('--lang=en-US')
  driver = uc.Chrome(options=options, use_subprocess=True, version_main=147)
  version = uc.Patcher()
  print('Webdriver version: ',version)
except (SessionNotCreatedException, TimeoutException, Exception) as er:
  print(f'[ERROR] driver doesn\'t run! {repr(er)}\n{er.msg}')
else:
  driver.get(RESPONDENT_LINK)
  driver.maximize_window()
  wait = WebDriverWait(driver, 10)
  # driver.switch_to.new_window('tab')
t.sleep(1)
# check lists length
if len(anchor_list_) == len(prices_list) and len(addresses_list) == len(prices_list):
  print('Lists length are equal')
# clear data
clear_addresses(addresses_list)
clear_prices(prices_list)

 # driver.find_elements(By.XPATH,value="//input[@type='text']")
# for _ in range(len(anchor_list_)):
for _ in range(0,1,1): # range(10)
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
          or button are non clickable xD {repr(er)}\n{er.msg}')

driver.refresh()
driver.switch_to.new_window('tab')
driver.refresh()
driver.get(SPREAD_CREATE_LINK)
rand_time()
try:
  login_button = wait.until(ec.element_to_be_clickable((By.XPATH,'//a[contains(text(),"Zaloguj się w")]')))
  # `//a[contains(text(),"Zaloguj się w\u00A0")]` with gravis (backticks ``) query in
  # console (browser F12) $x('...') interprets \u00A0 (unicode) as HTML &nbsp; for more info
  # look at tests.py file
  human_click(login_button)
  print('[INFO] login_button clicked')
  rand_time()
  # --------------- after this moment program doesn't work anymore --------- #
  # input_login = wait.until(ec.element_to_be_selected((By.XPATH,'//input[@type="email"]')))
  # input_login = wait.until(ec.element_to_be_selected(driver.find_element(By.ID,'//input[contains(@id,"identifier")]')))
  input_login = wait.until(ec.presence_of_all_elements_located((By.XPATH,"//input")))
  list_ = relentless_searcher(input_login)
  relentless_clicker(list_)


  """
  // Skoro jest aktywny, spróbuj mu po prostu "wlać" tekst do środka
  document.activeElement.value = "twoj_mail@gmail.com";
  // I teraz najważniejsze - musisz "szturchnąć" stronę, żeby zauważyła zmianę
  document.activeElement.dispatchEvent(new Event('input', { bubbles: true }));
  document.activeElement.dispatchEvent(new Event('change', { bubbles: true }));
  """
  script =  """
               document.activeElement.value = arguments[0];
               document.activeElement.dispatchEvent(new Event('input', { bubbles: true }));
               document.activeElement.dispatchEvent(new Event('change', { bubbles: true }));
            """
  script_ = """
              arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input', { bubbles: true })); arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
           """
  driver.execute_script(script,os.getenv("EMAIL"))
  print('script executed')

  # driver.execute_script("arguments[0].click();",input_login)
  # driver.execute_script(f"arguments[0].value = '{os.getenv("EMAIL")}'",input_login)
  # # action = ActionChains(driver)
  # action.move_to_element(input_login).click().perform()
  # input_login.click()
  # human_click(input_login)
  # input_login.send_keys(os.getenv("EMAIL"))
  rand_time()
  # input_login.send_keys(Keys.ENTER)
  print('[INFO] login typed')
  rand_time()
  input_password = wait.until(ec.presence_of_element_located((By.XPATH,'//input[@type="password"]')))
  input_password.send_keys(os.getenv("PASS"))
  rand_time()
  input_password.send_keys(Keys.ENTER)
  print('[INFO] password typed')
  rand_time()
  answers_button = wait.until(ec.presence_of_element_located((By.XPATH,'(//div[contains(text(),"Odpowiedzi")])[1]')))
  human_click(answers_button)
  print('[INFO] answers_button clicked')
  rand_time()
  display_in_spreadsheet = wait.until(ec.presence_of_element_located((By.XPATH,'//span[contains(text(),"Wyświetl w ")]')))
  human_click(display_in_spreadsheet)
  print('[INFO] display_button clicked')
except (TimeoutException, Exception) as er:
  print(f'[ERROR] something went wrong {repr(er)}\n{er}')
  # print(input_login)
  # print(type(input_login))
  # if input_login:
  #   print('True')
  # else:
  #   print('False')


_tactical_input = input('Give some cooKeys! :)')
