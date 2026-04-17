## ------------------ START ------------------- ##

import undetected_chromedriver as uc
import os
from constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, SessionNotCreatedException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as ec
import random as r, time as t
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class InstaFollower:
  def __init__(self):
    self.driver = None
    self.wait = None

  def test_run(self):
    try:
      options = uc.ChromeOptions()
      options.add_argument(f"--user-data-dir={os.getenv("CHROME_DRIVER_PATH")}")
      driver = uc.Chrome(options=options, use_subprocess=True, version_main=147)
      version = uc.Patcher()
      print('wersja webdrivera: ', version)
    except SessionNotCreatedException as er:
      print(f'[ERROR] function test_run(), line 17 {er}')
    except TimeoutException as er:
      print(f"The time is out my child :) {er}")
    else:
      self.driver = driver
      self.user_agent_ver()
      self.rand_time()
      self.driver.maximize_window()
      self.rand_time()
      self.driver.get(YT_URL)
      self.rand_time()
      self.driver.switch_to.new_window('tab')
      self.driver.get(GM_URL)
      self.rand_time()
      self.driver.switch_to.new_window('tab')
      self.driver.get(INSTA_URL)
      self.rand_time()
      wait = WebDriverWait(driver, 10)
      self.wait = wait
      print(self.wait, self.driver)
    print(self.wait, self.driver)

  def login(self):
    try:
      options = uc.ChromeOptions()
      options.add_argument(f"--user-data-dir={os.getenv("CHROME_DRIVER_PATH")}")
      driver = uc.Chrome(options=options, use_subprocess=True, version_main=147)
      version = uc.Patcher()
      print('Webdriver version: ',version)
    except (SessionNotCreatedException, TimeoutException, Exception) as er:
      print(f'[ERROR] driver doesn\'t run! {repr(er)}\n{er.msg}')
    else:
      self.driver = driver
      self.user_agent_ver()
      self.rand_time()
      self.driver.maximize_window()
      self.rand_time()
      self.driver.get(YT_URL)
      self.rand_time()
      self.driver.switch_to.new_window('tab')
      self.driver.get(GM_URL)
      self.rand_time()
      self.driver.switch_to.new_window('tab')
      self.driver.get(INSTA_URL)
      self.rand_time()
      wait = WebDriverWait(driver, 20)
      self.wait = wait

    # handles with cookie window
    try:
      decline_cookie = self.wait.until(ec.presence_of_element_located((By.XPATH,'//div/button[2]')))
    except (TimeoutException, Exception) as er:
      print(f'[INFO] Cookie window doesn\'t appear {repr(er)}\n{er.msg}')
    else:
      self.human_click(decline_cookie)
      self.rand_time()

    #inputs account login
    try:
      other_profile_button = self.wait.until(ec.presence_of_element_located((By.XPATH,'(//div/div[@role="button"])[4]')))
    except (TimeoutException, Exception) as er:
      print(f'[INFO] Window doesn\'t appear {repr(er)}\n{er.msg}')
    else:
      self.human_click(other_profile_button)
      self.rand_time()
    try:
      input_login = self.wait.until(ec.presence_of_element_located((By.XPATH,'//input[contains(@type,"text")]')))
    except (TimeoutException,Exception) as er:
      print(f'[ERROR] Can\'t type login  {repr(er)}\n{er.msg}')
    else:
      input_login.send_keys(os.getenv("INSTA_LOGIN"))
      self.rand_time()
      input_login.send_keys(Keys.TAB)
      self.rand_time()

      #inputs password
      input_password = self.wait.until(ec.presence_of_element_located((By.XPATH,'//input[contains(@type,"password")]')))
      input_password.send_keys(os.getenv("INSTA_PASSWORD"))
      self.rand_time()
      input_login.send_keys(Keys.ENTER)
      self.rand_time()

    # save your credentials (no)
    try:
      save_credentials_button = self.wait.until(ec.element_to_be_clickable((By.XPATH,'//div[contains(text(),"Nie teraz")]'))) # Polish - English => "Not now"
    except (TimeoutException, Exception) as er:
      print(f'[INFO] Window `save credentials` doesn\'t appear {repr(er)}\n{er.msg}')
    else:
      self.rand_time()
      self.human_click(save_credentials_button)
      print('Button clicked')

    # disable pop ups
    try:
      popup_disable_button = self.wait.until(ec.presence_of_element_located((By.XPATH,'//button[contains(text(),"Nie teraz")]'))) # Polish - English => "Not now"
    except (TimeoutException, Exception) as er:
      print(f'[INFO] Popup window doesn\'t appear {repr(er)}\n{er.msg}')
    else:
      self.human_click(popup_disable_button)
      print('Button clicked')

  def follow(self):
    try:
      # choose your favourite person you followed with xD !
      click_own_profile_button = self.wait.until(
      ec.presence_of_element_located((By.XPATH,'(//div[@data-visualcompletion="ignore-dynamic"])[3]/div[8]//a')))
      self.rand_time()
      click_own_profile_button.send_keys(Keys.ENTER)
      self.rand_time()
      click_following_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Obserwowani")]/ancestor::a/ancestor::div[1]'))) # Polish - English => "Following"
      self.rand_time()
      click_following_buttons = click_following_button.find_elements(By.XPATH, '//span[contains(text(),"Obserwowani")]/ancestor::a/ancestor::div[1]//*') # Polish - English => "Following"
      list_ = self.relentless_searcher(click_following_buttons)
      self.relentless_clicker(list_)
      self.rand_time()
      click_search_ = self.wait.until(ec.presence_of_element_located((By.XPATH, '//input[contains(@aria-label,"Pole wejściowe")]')))
      self.rand_time()
      click_search_.send_keys(FAVOURITE_PERSON1)
      self.rand_time()
      click_fav_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, f'(//a[contains(@href,"{FAVOURITE_ACCOUNT_HREF1}")])[1]')))
      self.rand_time()
      click_fav_button.send_keys(Keys.ENTER)
      self.rand_time()
      # choose her/his followers
      choose_her_followers_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"obserwujących")]')))
      self.rand_time()
      choose_her_followers_buttons = choose_her_followers_button.find_elements(By.XPATH,'//span[contains(text(),"obserwujących")]/ancestor::a/ancestor::div[1]//*')
      list_ = self.relentless_searcher(choose_her_followers_buttons)
      self.relentless_clicker(list_)
    except (TimeoutException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException, AttributeError, ValueError, Exception) as er:
      print(f'[ERROR] Something went wrong {repr(er)}\n{er.msg}')

  def scroller(self):
    """Scroll it! Scroll it properly and righteous! """
    try:
      path = '//div[contains(@role,"dialog")]/div/div/div/div/div[3]'
      # path = '//div[contains(@role,"dialog")]'
      modal = self.wait.until(ec.presence_of_element_located((By.XPATH,path)))

      for _ in range(1,4,1): # range(4) is the same
        self.driver.execute_script("arguments[0].scrollTo({top: arguments[0].scrollTop + 400, behavior: 'smooth'});", modal)
        self.rand_time()
      for _ in range(1,4,1): # range(4) is the same
        self.driver.execute_script("arguments[0].scrollTo({top: arguments[0].scrollTop - 400, behavior: 'smooth'});", modal)
        self.rand_time()

    except (TimeoutException, ElementClickInterceptedException,StaleElementReferenceException,ElementNotInteractableException, ValueError,AttributeError, Exception) as er:
      print(f'[ERROR] function scroller(), line 185, repr(): {repr(er)}\n message: {er.msg}') # er.msg for Selenium, standard errors er.args[0], repr() return only error class eg. `InvalidSelectorException()`

  def follower(self):
    """ Follow them all! Nope, only four :)"""
    try:
      buttons = self.driver.find_elements(By.XPATH, value='//div[contains(text(),"Obserwuj")]/ancestor::div[1]/ancestor::button')
      i = 0
      for _ in buttons[:4]:
        i += 1
        self.rand_time()
        self.human_click(_)
    except (TimeoutException, ElementClickInterceptedException,StaleElementReferenceException,ElementNotInteractableException, ValueError,AttributeError, Exception) as er:
      print(f'[ERROR] function follower(), line 196, repr: {repr(er)}\n nor: {er.msg}')

  def find_followers(self):
    try:
      path = '//div[contains(@role,"dialog")]/div/div/div/div/div[3]'
      modal = self.wait.until(ec.presence_of_element_located((By.XPATH,path)))

      for _ in range(1,4,1): # range(4) is the same
        self.driver.execute_script("arguments[0].scrollTo({top: arguments[0].scrollTop + 400, behavior: 'smooth'});", modal)
        self.rand_time()
      for _ in range(1,4,1): # range(4) is the same
        self.driver.execute_script("arguments[0].scrollTo({top: arguments[0].scrollTop - 400, behavior: 'smooth'});", modal)
        self.rand_time()

    except (TimeoutException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException, ValueError, AttributeError, Exception) as er:
      print(f'[ERROR] function scroller(),  repr(): {repr(er)}\n message: {er.msg}')

    self.rand_time()

    try:
      buttons = self.driver.find_elements(By.XPATH, value='//div[contains(text(),"Obserwuj")]/ancestor::div[1]/ancestor::button')
      i = 0
      for _ in buttons[:4]:
        i += 1
        self.rand_time()
        self.human_click(_)
    except (TimeoutException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException, ValueError, AttributeError, Exception) as er:
      print(f'[ERROR] function follower(), line 196, repr: {repr(er)}\n nor: {er.msg}')

  def rand_time(self):
    x = r.uniform(1.2,3)
    y = r.uniform(5.5,8.5)
    return t.sleep(r.uniform(a=x, b=y))

  def user_agent_ver(self):
    """ returns user-agent """
    ua = self.driver.execute_script("return navigator.userAgent")
    print(f"User-Agent: {ua}")

  def human_click(self, element):
    """ standard Selenium .click() always point at x=0,y=0
    middle of the button  """
    # fetching button size
    width = element.size['width']
    height = element.size['height']
    # randomize offset, 20-70% of button size
    offset_x = r.randint(int(width * 0.2), int(width * 0.7)) - (width / 2)
    offset_y = r.randint(int(height * 0.2), int(height * 0.7)) - (height / 2)
    # make a move !
    action = ActionChains(self.driver)
    action.move_to_element_with_offset(element, offset_x, offset_y)
    action.click()
    action.perform()
    print(f"Button hit at: {offset_x}, {offset_y}")

  def relentless_searcher(self,object):
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

  def relentless_clicker(self, list_):
    """Click them all!"""
    index = 0
    for _ in list_:
      index += 1
      name = _.tag_name
      # sends click
      try:
        self.human_click(_)
        self.rand_time()
        print(f'[INFO] Clicked! {index} {name}')
      except (ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException, Exception) as er:
        print(f'[INFO] Can\'t click them! {index}')
      else:
        print(f'[INFO] object: {index} is clickable ')
      # sends Enter
      try:
        _.send_keys(Keys.ENTER)
        self.rand_time()
        print(f'[INFO] Object {index} {name} Entered!')
      except (ElementClickInterceptedException,StaleElementReferenceException,ElementNotInteractableException, Exception) as er:
        print(f'[INFO] Can\'t use ENTER on object {index} {repr(er)}')
      else:
        print(f'[INFO] object: {index} is enterable ')

        ## ---------------- THE END ------------------- ##
