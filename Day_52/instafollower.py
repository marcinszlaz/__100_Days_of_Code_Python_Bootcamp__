import undetected_chromedriver as uc
import os
from constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, SessionNotCreatedException, ElementClickInterceptedException, StaleElementReferenceException
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
      wait = WebDriverWait(driver, 20)
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
        ec.presence_of_element_located((By.XPATH,'(//div[@data-visualcompletion="ignore-dynamic"])[3]/div[8]' )))
      # '(//div[@data-visualcompletion="ignore-dynamic"])[3]/div[8]'
      # '//img[contains(@alt,"jankk0walsky")]'
      self.rand_time()
      self.human_click(click_own_profile_button)
      self.rand_time()
      click_following_button = self.wait.until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Obserwowani")]')))
      self.rand_time()
      self.human_click(click_following_button)
      self.rand_time()
      click_search_ = self.wait.until(
        ec.presence_of_element_located((By.XPATH, '//input[contains(@aria-label,"Pole wejściowe")]')))
      self.rand_time()
      click_search_.send_keys(FAVOURITE_PERSON)
      self.rand_time()
      click_fav_button = self.wait.until(
        ec.element_to_be_clickable((By.XPATH, f'(//a[contains(@href,"{FAVOURITE_ACCOUNT_HREF}")])[1]')))
      # click_fav_button = self.wait.until(ec.element_to_be_clickable((By.XPATH,f'(//a[contains(@href,"/antsy__pantsy/")])[1]')))
      self.rand_time()
      self.human_click(click_fav_button)
      self.rand_time()
      # choose her/his followers
      choose_her_followers_button = self.wait.until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"obserwujących")]')))
      self.rand_time()
      self.human_click(choose_her_followers_button)
      self.rand_time()
    except (TimeoutException, AttributeError, ValueError) as er:
      print(f'Something went wrong but It\'s ok xD {er}')
    input("Strategic debugging input")

  def find_followers(self):
    self.rand_time()
    dialog_button_xd = self.wait.until(ec.presence_of_element_located((By.XPATH,'//div[contains(@role,"dialog")]')))
    self.rand_time()
    self.human_click(dialog_button_xd)
    self.rand_time()
    dialog_button_xd.send_keys(Keys.TAB)
    self.rand_time()
    dialog_button_xd.send_keys(Keys.TAB)
    self.rand_time()
    dialog_button_xd.send_keys(Keys.ESCAPE)
    self.rand_time()
    for _ in range(r.randint(2,5)):
      dialog_button_xd.send_keys(Keys.PAGE_DOWN)
      self.rand_time()
    dialog_button_xd.send_keys(Keys.HOME)
    self.rand_time()
    following_button = self.wait.until(ec.presence_of_all_elements_located((By.XPATH,'//div[contains(text(),"Obserwuj")]')))
    self.rand_time()
    for _ in range(1,4):
      self.human_click(following_button[_])
      self.rand_time()

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

  def relentless_clicker(self):
    list_ = ['(//div/div[@role="button"])[4]', '//span[contains(text(),"Kontynuuj")]']
    for _ in list_:
      other_profile_button = self.wait.until(ec.presence_of_element_located((By.XPATH, f"{_}")))
      try:
        other_profile_button.send_keys(Keys.ENTER)
        self.rand_time()
        print('Clicked ENTER !')

      except (ElementClickInterceptedException,StaleElementReferenceException) as er:
        print('Can\'t use ENTER')
      else:
        try:
          other_profile_button.send_keys(Keys.TAB)
          self.rand_time()
        except (ElementClickInterceptedException,StaleElementReferenceException) as er:
          print('Can\'t use TAB')
        else:
          try:
            self.human_click(other_profile_button)
            self.rand_time()
          except (ElementClickInterceptedException,StaleElementReferenceException, ValueError) as er:
            print('Other error, Can\'t even click !')


"""
  def get_internet_speed(self):
    
    # open browser
    try:
      options = uc.ChromeOptions()
      options.add_argument(f"--user-data-dir={os.getenv("CHROME_DRIVER_PATH")}")
      # driver = uc.Chrome(options=options)
      driver = uc.Chrome(options=options, use_subprocess=True, version_main=147)
      version = uc.Patcher()
      print('wersja webdrivera: ',version)
    except SessionNotCreatedException as er:
      print('[ERROR]')
    else:
      self.driver = driver
      self.user_agent_ver()
      driver.maximize_window()
      driver.get(SPEED_TEST_URL)
      wait = WebDriverWait(driver, 20)
      self.wait = wait

    # cookie handler
    try:
      cookie_accept_handler = self.wait.until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="banner-actions-"]  button[id^="onetrust-accept"]')))
    except TimeoutException as ve:
      print(f'[ERROR] probably cookies was accepted before \\ve\\')
    except AttributeError as ae:
      print(f"It's fine {ae}")
    else:
      t.sleep(r.uniform(1.5, 3))
      # cookie_accept_handler.click()
      self.human_click(cookie_accept_handler)

    # starting tests
    try:
      start_test = wait.until(ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')))
    except ValueError as ve:
      print(f"[ERROR] while clicking `start` speed testing {ve}")
    else:
      t.sleep(r.uniform(1.5, 3))
      # start_test.click()
      self.human_click(start_test)
      t.sleep(60)

    # reading values
    try:
      speed_data = wait.until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[class*="result-data-large"]')))
    except TimeoutException as ve:
      print(f'[ERROR] unreadable ones, timeout error ! {ve}')
    except ValueError as ve:
      print(f'[ERROR] unreadable ones, other error ! {ve}')
    else:
      self.download = speed_data[0].text
      self.upload = speed_data[1].text
      print('Download: ', self.download)
      print('Upload: ', self.upload)
      return f"Download: {self.download}\n Upload: {self.upload}"

  def tweet_at_provider(self):
    t.sleep(r.uniform(0.5,3))
    self.driver.switch_to.new_window('tab')
    t.sleep(r.uniform(0.7,3.5))
    self.driver.get("https://mail.google.com")
    t.sleep(r.uniform(1.2,2.8))
    self.driver.switch_to.new_window('tab')
    t.sleep(r.uniform(1,3))
    self.driver.get(TWITTER_URL)

    # part of code responsible for login is commented
    # cos of constant captcha & 2FA, we just use cookies, browser will remember our password xD
    try:
      input_email = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,'input[class^="r-30o5oe"]')))
    except TimeoutException as ve:
      print('We can"\t find input form we"ll try using xpath')
    except ValueError as ve:
      print('[ERROR] occurred xD')
    else:
      t.sleep(r.uniform(0.6,2))
      input_email.send_keys(os.getenv("TWITTER_LOGIN"))
      t.sleep(r.uniform(1,3))
      input_email.send_keys(Keys.ENTER)
      try:
        next_input = self.wait.until(ec.element_to_be_clickable((By.XPATH,'//div[contains(@class,"css-")]/button[2]')))
      except TimeoutException as ve:
        print("It's ok :-) ")
      except ValueError as ve:
        print("It's ok :-) ")
      else:
        if next_input:
          self.human_click(next_input)
    try:
      input_password = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,'input[data-testid="ocfEnterTextTextInput"]')))
    except TimeoutException as te:
      print("It's ok :-) ")
    else:
      t.sleep(r.uniform(1, 3))
      input_password.send_keys(os.getenv("TWITTER_PASSWORD"))
      t.sleep(r.uniform(0.6, 2))
      input_password.send_keys(Keys.ENTER)
      t.sleep(r.uniform(0.2, 1))
   

    post = self.wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')))
    t.sleep(r.uniform(0.2,4))
    self.human_click(post)
    msg = f"Hey Internet Provider, why is my Internet speed {self.download}down/{self.upload}up when I pay for 15down/20up?"
    post_input = self.wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
    t.sleep(r.uniform(0.4,2))
    post_input.send_keys(msg)
    t.sleep(r.uniform(0.4,4))
    post_enter = self.wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')))
    self.human_click(post_enter)


  def human_click(self, element):
    # fetching button size
    width = element.size['width']
    height = element.size['height']

    # randomize offset, 20-80% of button size
    offset_x = r.randint(int(width * 0.2), int(width * 0.6)) - (width / 2)
    offset_y = r.randint(int(height * 0.2), int(height * 0.8)) - (height / 2)

    # make a move !
    action = ActionChains(self.driver)
    action.move_to_element_with_offset(element, offset_x, offset_y)
    action.click()
    action.perform()
    print(f"clicked with offset: {offset_x}, {offset_y}")

"""

