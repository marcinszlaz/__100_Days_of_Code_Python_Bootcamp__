# TODO input values to function choose_class(), multiple values, days and times,
# TODO maybe args* or kwargs**, or more simply way, using list
# TODO even simplier, only 3 args for choose_class() but make input() in while loop

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os,pathlib
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import random as r, time as t
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys # you can use keys on www with this black magic library

GYM_URL="https://appbrewery.github.io/gym/"
class_list = []
class_dict = {}
booked_dict = {"_counter_":0}
booked = 0
waitlisted = 0
alr_bok_wait = 0  # already booked waitlisted

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
  num = 0
  for _time in class_times:
    num += 1
    class_date = _time.find_element(By.XPATH, value= './ancestor::div[4]/h2')
    class_name = _time.find_element(By.XPATH, value = './preceding-sibling::h3')
    # t.sleep(0.2)
    # './ancestor::div[2]/div[2]/button[starts-with(@id,"book-button-")]'
    # './ancestor::div[1]/following-sibling::div/button[starts-with(@id,"book-button-")]'
    button = _time.find_element(By.XPATH,value= './ancestor::div[1]/following-sibling::div/button[starts-with(@id,"book-button-")]')
    class_list.append((f'Booked: {class_name.text} on {class_date.text} at {_time.text}',button))
    class_dict[f'class_{num}']={"class_name": class_name.text, "class_date": class_date.text, "class_hour":_time.text, "button_object": button}

def check_bookings():
  global booked_dict
  booking = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[id^="my-bookings-"]')))
  booking.click()
  try:
    confirmed_bookings_presence = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,'h2[id^="confirmed-bookings-"]')))
    confirmed_waitlist_presence = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,'h2[id*="waitlist-title"]')))
  except TimeoutException as te:
    print(f"Booking or waitlist probably are empty")
  else:
    if confirmed_bookings_presence:
      class_name = driver.find_elements(By.CSS_SELECTOR,value="h3[id*='booking-class-name-']")
      num = 0
      for _class in class_name:
        num+=1
        when = _class.find_elements(By.XPATH,value="./following-sibling::p[1]")
        button = _class.find_elements(By.XPATH,value='./ancestor::div/following-sibling::button[contains(@id,"cancel-booking-")]')
        booked_dict[f'booked_{num}']={"name":_class.text,"date":when[6:-8],"time":when[-8:],"button":button}
        booked_dict["bk_counter"]=num
        booked_dict["_counter_"]=int(booked_dict.get("bk_counter",0))+int(booked_dict.get("wt_counter",0))
    if confirmed_waitlist_presence:
      waitlist_name = driver.find_elements(By.XPATH, value='//h3[starts-with(@id,"waitlist-class-name")]')
      num_ = 0
      for _waitlist in waitlist_name:
        num_+=1
        when = _waitlist.find_elements(By.XPATH,value="./following-sibling::p[1]")
        button = _waitlist.find_elements(By.XPATH,value='./ancestor::div[1]/following-sibling::button[starts-with(@id,"leave-waitlist-")]')
        booked_dict[f'waitlisted_{num_}']= {"name":_waitlist.text,"date":when[6:-8],"time":when[-8:],"button":button}
        booked_dict["wt_counter"] = num_
        booked_dict["_counter_"] = int(booked_dict.get("bk_counter", 0)) + int(booked_dict.get("wt_counter", 0))

def choose_class(c_list: list,day='Tue',time='6:00 PM'):
  global booked, waitlisted, alr_bok_wait
  new_waitlist = "[New Waitlist] "
  new_booking = "[New Booking] "
  hour_list = ['7:00 am','8:00 am','9:00 am','5:00 pm','6:00 pm','7:00 pm']
  day_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
  if day[:3].lower() not in day_list and time.lower() not in hour_list:
    print(f'Sorry, correct values are {day_list}/{hour_list}')
    answer = input('Wanna try again ? (y/n)')
    if answer.lower() == "y":
      day = input("Type day\n")
      time = input("Type hour\n")
      choose_class(c_list,day,time)
    else:
      print("Bye\n")
      driver.close()
      driver.quit()
      #raise ValueError("[ERROR] User doesn't cooperate xD. Incorrect values, this is the end")
  for _ in c_list:
    if day[:3].lower() in _[0].lower() and time.upper() in _[0].upper():
      if _[1].text.lower() == "booked":
        print(f'Already {_[0]}')
        booked+=1
      elif _[1].text.lower() == "waitlisted":
        print(f'Already on Waitlist => {_[0].replace('Booked:','')}')
        waitlisted+=1
      elif _[1].text.lower() == "join waitlist":
        _[1].click() # second value in tuple is button object (Selenium)
        print(f'Joined waitlist for: {_[0].replace('Booked:','')}')
        new_waitlist = "".join([new_waitlist, _[0].replace('Booked: ','')])
      else:
        _[1].click() # second value in tuple is button object (Selenium)
        print(f'{_[0]}')
        new_booking = "".join([new_booking,_[0].replace('Booked: ', '')])
  check_bookings()
  alr_bok_wait = booked_dict["_counter_"]
  print("\n--- BOOKING SUMMARY ---")
  print(f'Classes booked: {booked}')
  print(f'Waitlists joined: {waitlisted}')
  print(f'Already booked/waitlisted: {alr_bok_wait}')
  print(f'Total Tuesday & Thursday 6pm classes: {alr_bok_wait}')
  print("\n--- DETAILED CLASS LIST ---")
  print(new_booking)
  print(new_waitlist)

def booking_summary():
  """function booking_summary is obsolete, instead of it use function choose_class,
     choose_class takes features from function booking_summary"""
  global booked,waitlisted, alr_bok_wait
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
again = ""
while again != "exit":
  new_whole_class()
  day = input("Type day\n")
  time = input("Type hour\n")
  choose_class(class_list,day,time)
  again = input("Add next training unit ? (any key - yes / exit - no\n")
  # if again == "exit":
  #   driver.quit()

# booking_summary()
# whole_class()
# yoga_class()
# hiit_class()
# spin_class()
# driver.implicitly_wait(0)
