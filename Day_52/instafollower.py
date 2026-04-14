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
      print('[ERROR]')
    except TimeoutException as er:
      print("The time is out my child :)")
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
      print('wersja webdrivera: ',version)
    except SessionNotCreatedException as er:
      print('[ERROR] driver doesn\'t run !')
    except TimeoutException as er:
      print("The time is out my child :)")
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

    # cookie
    try:
      decline_cookie = self.wait.until(ec.presence_of_element_located((By.XPATH,'//div/button[2]')))
      # /html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]
      # '//div/button[contains(text(),"opcjonalne pliki cookie")]'
    except (ValueError, TimeoutException) as er:
      print('Cookie resisting !')
    else:
      self.human_click(decline_cookie)
      self.rand_time()
      decline_cookie.send_keys(Keys.ENTER)
      self.rand_time()
    #input login
    try:
      other_profile_button = self.wait.until(ec.presence_of_element_located((By.XPATH,'(//div/div[@role="button"])[4]')))
    except (TimeoutException, ValueError) as er:
      print('Window doesn\'t appear')
    else:
      self.human_click(other_profile_button)
      other_profile_button.send_keys(Keys.ENTER)
      self.rand_time()
    # input('Uzyj innego profilu')
    self.rand_time()
    try:
      input_login = self.wait.until(ec.presence_of_element_located((By.XPATH,'//input[contains(@type,"text")]')))
    # '//input[contains(@id,"_r_2_")]'
    except (TimeoutException,ValueError) as er:
      print('It\'s ok xD')
    else:
      input_login.send_keys(os.getenv("INSTA_LOGIN"))
      self.rand_time()
      input_login.send_keys(Keys.TAB)
      self.rand_time()
      #input password
      input_password = self.wait.until(ec.presence_of_element_located((By.XPATH,'//input[contains(@type,"password")]')))
      input_password.send_keys(os.getenv("INSTA_PASSWORD"))
      self.rand_time()
      input_login.send_keys(Keys.ENTER)
      self.rand_time()
    # save your credentials (no)
    try:
      save_credentials_button = self.wait.until(ec.element_to_be_clickable((By.XPATH,'//div[contains(text(),"Nie teraz")]')))
    except (TimeoutException, ValueError) as er:
      print(f'It\'s ok :) {er}')
    else:
      self.rand_time()
      self.human_click(save_credentials_button)
      print('clicked')
      save_credentials_button.send_keys(Keys.ENTER)
      print('entered')
    # disable pop ups
    try:
      popup_disable_button = self.wait.until(ec.presence_of_element_located((By.XPATH,'//button[contains(text(),"Nie teraz")]')))
    except TimeoutException as er:
      print('It\'s ok :)')
    else:
      self.human_click(popup_disable_button)
      print('clicked')
      popup_disable_button.send_keys(Keys.ENTER)
      print("entered")

  def follow(self):
    try:
      # choose your favourite person you followed with xD !
      click_own_profile_button = self.wait.until(
      ec.presence_of_element_located((By.XPATH,'(//div[@data-visualcompletion="ignore-dynamic"])[3]/div[8]//a' )))
      self.rand_time()
      click_own_profile_button.send_keys(Keys.ENTER)
      # self.human_click(click_own_profile_button)
      self.rand_time()
      click_following_button = self.wait.until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Obserwowani")]/ancestor::a/ancestor::div[1]')))
      self.rand_time()
      click_following_buttons = click_following_button.find_elements(By.XPATH, '//span[contains(text(),"Obserwowani")]/ancestor::a/ancestor::div[1]//*')
      list_ = self.relentless_searcher(click_following_buttons)
      self.relentless_clicker(list_)
      # click_following_button.send_keys(Keys.ENTER)
      # click_following_button.click()
      # self.human_click(click_following_button)
      self.rand_time()
      click_search_ = self.wait.until(
        ec.presence_of_element_located((By.XPATH, '//input[contains(@aria-label,"Pole wejściowe")]')))
      self.rand_time()
      click_search_.send_keys(FAVOURITE_PERSON1)
      self.rand_time()
      click_fav_button = self.wait.until(
        ec.element_to_be_clickable((By.XPATH, f'(//a[contains(@href,"{FAVOURITE_ACCOUNT_HREF1}")])[1]')))
      '//a[contains(@href,"trash")][1]'
      self.rand_time()
      click_fav_button.send_keys(Keys.ENTER)
      # self.human_click(click_fav_button)
      self.rand_time()
      # choose her/his followers
      choose_her_followers_button = self.wait.until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"obserwujących")]')))
      choose_her_followers_buttons = choose_her_followers_button.find_elements(By.XPATH,'//span[contains(text(),"obserwujących")]/ancestor::a/ancestor::div[1]//*')
      list_ = self.relentless_searcher(choose_her_followers_buttons)
      self.relentless_clicker(list_)
      # self.human_click(choose_her_followers_button)
      # self.rand_time()
    except (TimeoutException, AttributeError, ValueError,ElementClickInterceptedException,StaleElementReferenceException,ElementNotInteractableException) as er:
      print(f'Something went wrong but It\'s ok xD {er}')
    # input("Strategic debugging input")

  def find_followers(self):

    '''# Source - https://stackoverflow.com/a/42539537
# Posted by taha mokfi
# Retrieved 2026-04-14, License - CC BY-SA 3.0

scr1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]')
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

ulepszona wersja:
# To jest czysta magia JS wewnątrz Selenium
driver.execute_script("arguments[0].scrollTo({top: arguments[0].scrollTop + 400, behavior: 'smooth'});", scr1)
'''
    # try:
    buttons = self.driver.find_elements(By.XPATH,value='//div[contains(text(),"Obserwuj")]/ancestor::div[1]/ancestor::button')
    i = 0
    for _ in buttons[:4]:
      i+=1
      self.rand_time()
      self.human_click(_)
    # except (TimeoutException, AttributeError, ValueError,ElementClickInterceptedException,StaleElementReferenceException,ElementNotInteractableException) as er:
    #   print('Ooops :) while following')

    # try:
    #   modal = self.wait.until(ec.presence_of_element_located((By.XPATH, '//div[contains(@role,"dialog")]')))
    #   for _ in range(1,4):
    #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    #     self.rand_time()
    # except (TimeoutException, AttributeError, ValueError,ElementClickInterceptedException,StaleElementReferenceException,ElementNotInteractableException) as er:
    #   print('Ooops :) while scrolling')

  def rand_time(self):
    x = r.uniform(1.2,3)
    y = r.uniform(5.5,8.5)
    return t.sleep(r.uniform(a=x, b=y))

  def user_agent_ver(self):
    ua = self.driver.execute_script("return navigator.userAgent")
    print(f"User-Agent: {ua}")

  def human_click(self, element):
    # fetching button size
    width = element.size['width']
    height = element.size['height']

  def relentless_searcher(self,object):
    """ function takes selenium iterable object and return list
    of objects ready to click or enter, you may cal me stupid, why I make my own list ?
     because I don't trust Selenium objects, that is why xD """
    tmp_list = []
    index = 0
    for _ in object:
      index+=1
      tmp_list.append(_)
      print(f'obj:{index} {_}')
    return tmp_list

  def relentless_clicker(self,list_):
    index = 0
    for _ in list_:
      index +=1
      name = _.tag_name
      try:
        _.send_keys(Keys.ENTER)
        self.rand_time()
        print(f'obj {index} {name} Entered!')
      except (ElementClickInterceptedException,StaleElementReferenceException,ElementNotInteractableException, ValueError) as er:
        print(f'Can\'t use ENTER obj {index}')
      else:
        print(f'obj: {index} is enterable ')
      try:
        self.human_click(_)
        self.rand_time()
        print(f'Clicked! {index} {name}')
      except (ElementClickInterceptedException,StaleElementReferenceException,ElementNotInteractableException,ValueError) as er:
        print(f'Can\'t click them! {index}')
      else:
        print(f'obj: {index} is clickable ')

