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
class_list = []
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

def general_schedule():
  # whole div with schedule
  schedule_plan = wait.until(ec.presence_of_element_located((By.ID,"schedule-page")))
  # child divs with classes
  plan_blocks = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'div[id^="day-group-"]')))

"""
# css_selector div[class^/class*/class$="blahblah"] find div with class named blahblah ^start with *contain anywhere $end with
# xpath ancestor::div finds higher divs, child::p finds lower p
# xpath following-sibling::p lower neighbour in DOM, preceding-sibling::h5 higher neighbour in DOM
# you can use index [1] [last()] [first()]
# parent:: 1 lvl up only, descendant:: lower lvls
# xpath has own language, in web browser you can use
# $x('xpath request') in console (F12)
# example $x('//p/ancestor::div')
# $$ elements $ element (like find_element[s] in Selenium)
# $('p[id^="zupa"]') or $$('css-selector') in general
# xpath is mighty, but it's next programming language
# which I have to learn xDDD
# '//p[starts-with(@id,"class-time-yoga-")]/ancestor::div[4]/h2'
# you can't use ^ * $ u need to use starts-with(), contains(),
# count(), ends-with() exist in xpath 2.0 but it isn't supported
# substring(), string-length()
# //p[substring(@id, string-length(@id) - string-length('yoga') + 1) = 'yoga']
# xpath doesn't have index[0], starts with [1], is case sensitive
# and dot `.` means function text() -[fetching text from tag] and
# it means too, here, get from here, like in GNU-Linux OS ./ .
"""
def yoga_class():
  yoga_classes = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'p[id^="class-time-yoga-"]')))
  class_times = wait.until(ec.presence_of_all_elements_located((By.XPATH, '//p[starts-with(@id,"class-time-yoga-")]/ancestor::div[4]/h2')))

  yoga_classes_l = [_class for _class in yoga_classes]
  class_times_l =[_class for _class in class_times]

  # without checking length, zip takes care of this
  for _class,_name in zip(yoga_classes_l, class_times_l):
    print('yoga class at: ',_class.text,_name.text)

def hiit_class():
  hiit_classes = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'p[id^="class-time-hiit-"]')))
  class_times = wait.until(ec.presence_of_all_elements_located((By.XPATH,'//p[starts-with(@id,"class-time-hiit-")]/ancestor::div[4]/h2')))

  hiit_classes_l = [_class for _class in hiit_classes]
  class_times_l =[_class for _class in class_times]

  # without checking length, zip takes care of this
  for _class,_name in zip(hiit_classes_l, class_times_l):
    print('hiit class at: ',_class.text,_name.text)

def spin_class():
  spin_classes = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'p[id^="class-time-spin-"]')))
  class_times = wait.until(
    ec.presence_of_all_elements_located((By.XPATH, '//p[starts-with(@id,"class-time-spin-")]/ancestor::div[4]/h2')))

  spin_classes_l = [_class for _class in spin_classes]
  class_times_l = [_class for _class in class_times]

  # without checking length, zip takes care of this
  for _class, _name in zip(spin_classes_l, class_times_l):
    print('spin class at: ',_class.text, _name.text)

def whole_class():
  global class_list
  class_times = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'p[id^="class-time-"]')))
  class_dates = wait.until(ec.presence_of_all_elements_located((By.XPATH, '//p[starts-with(@id,"class-time-")]/ancestor::div[4]/h2')))
  class_names = wait.until(ec.presence_of_all_elements_located((By.XPATH, '//p[starts-with(@id,"class-time-")]/preceding-sibling::h3')))

  class_times_l = [_class for _class in class_times]
  class_dates_l = [_class for _class in class_dates]
  class_names_l = [_class for _class in class_names]

  # without checking length, zip takes care of this
  for _class,_date,_name in zip(class_times_l, class_dates_l, class_names_l):
    # print(f'Booked: {_name.text} on {_date.text} at {_class.text}')
    class_list.append(f'Booked: {_name.text} on {_date.text} at {_class.text}')

def new_whole_class():
  global class_list
  class_times = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'p[id^="class-time-"]')))
  for _time in class_times:
    class_date = _time.find_element(By.XPATH, value= './ancestor::div[4]/h2')
    class_name = _time.find_element(By.XPATH, value = './preceding-sibling::h3')
    # t.sleep(0.2)
    # './ancestor::div[2]/div[2]/button[starts-with(@id,"book-button-")]'
    # './ancestor::div[1]/following-sibling::div/button[starts-with(@id,"book-button-")]'
    button = _time.find_element(By.XPATH,value= './ancestor::div[1]/following-sibling::div/button[starts-with(@id,"book-button-")]')
    class_list.append((f'Booked: {class_name.text} on {class_date.text} at {_time.text}',button))

def choose_class(c_list: list,day='Tue',time='6:00 PM'):
  hour_list = ['7:00 AM','8:00 AM','9:00 AM','5:00 PM','6:00 PM','7:00 PM']
  day_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
  if day not in day_list and time not in hour_list:
    print(f'Sorry, correct values are {day_list}/{hour_list}')
    answer = input('Wanna try again ? (y/n)')
    if answer.lower() == "y":
      day = input("Type day")
      time = input("Type hour")
      choose_class(c_list,day,time)
    else:
      driver.quit()
      raise ValueError("Incorrect values, this is the end")
  for _ in c_list:
    if day in _[0] and time in _[0]:
      if _[1].text.lower() == "booked":
        print(f'Already {_[0]}')
      elif _[1].text.lower() == "waitlisted":
        print(f'Already on Waitlist => {_[0].replace('Booked:','')}')
      elif _[1].text.lower() == "join waitlist":
        _[1].click() # second value in tuple is button object (Selenium)
        print(f'Joined waitlist for: {_[0].replace('Booked:','')}')
      else:
        _[1].click() # second value in tuple is button object (Selenium)
        print(f'{_[0]}')

def booking_summary(): # it's better to do it inside choose_class, at least counters, then it will be closer to truth
  booked = 0
  waitlisted = 0
  alr_bok_wait = 0 # already booked waitlisted
  buttons = wait.until(ec.presence_of_all_elements_located((By.XPATH, '//button[starts-with(@id,"book-button-")]')))
  for button in buttons:
    if button.text.lower() == "booked":
      booked+=1
      alr_bok_wait+=booked
    if button.text.lower() == "waitlisted":
      waitlisted+=1
      alr_bok_wait+=waitlisted

  print("--- BOOKING SUMMARY ---")
  print(f'Classes booked: {booked}')
  print(f'Waitlists joined: {waitlisted}')
  print(f'Already booked/waitlisted: {alr_bok_wait}')

# core xD
login()
new_whole_class()
choose_class(class_list)
booking_summary()

# whole_class()
# yoga_class()
# hiit_class()
# spin_class()
# driver.implicitly_wait(0)
