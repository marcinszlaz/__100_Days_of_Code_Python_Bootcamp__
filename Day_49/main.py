from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os,pathlib
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time as t
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

GYM_URL="https://appbrewery.github.io/gym/"
class_list = []
class_dict = {}
booked_dict = {"_counter_":0}
booked = 0
waitlisted = 0
already_booked_waitlisted = 0
alt_alr_bok_wait = 0

# path to web browser user profile
user_data_dir = pathlib.Path.cwd() / "chrome_profile"

# login and password from .env
auth_path = pathlib.Path.cwd() / ".env"
load_dotenv(dotenv_path=auth_path)

chrome_options: Options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--start-maximized")

driver: WebDriver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)
wait = WebDriverWait(driver, 5)

def login():
  login_button = wait.until(ec.element_to_be_clickable((By.ID,"login-button")))
  login_button.click()
  print('login button clicked')
  email_input = wait.until(ec.presence_of_element_located((By.ID,"email-input")))
  email_input.clear()
  email_input.send_keys(os.getenv(key="ACCOUNT_EMAIL"))
  password_input = wait.until(ec.presence_of_element_located((By.ID,"password-input")))
  password_input.clear()
  password_input.send_keys(os.getenv(key="ACCOUNT_PASSWORD"))
  print('credentials typed')
  submit_button = wait.until(ec.element_to_be_clickable((By.ID,"submit-button")))
  submit_button.click()
  print('Am I logged? :',amilogged())

def amilogged():
  schedule_page = wait.until(ec.presence_of_element_located((By.ID,"schedule-page")))
  if not schedule_page:
    return False
  else:
    return True

def new_whole_class():
  global class_list
  class_list =[]
  class_schedule = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'a[id*="schedule-link"]')))
  class_schedule.click()
  class_times = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'p[id^="class-time-"]')))
  num = 0
  for _time in class_times:
    num += 1
    class_date = _time.find_element(By.XPATH, value= './ancestor::div[4]/h2')
    class_name = _time.find_element(By.XPATH, value = './preceding-sibling::h3')
    button = _time.find_element(By.XPATH,value= './ancestor::div[1]/following-sibling::div/button[starts-with(@id,"book-button-")]')
    t.sleep(0.15)
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
  class_schedule = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#schedule-link')))
  class_schedule.click()

def choose_class(c_list: list,day='Tue',time='6:00 PM')->None:
  global booked, waitlisted, already_booked_waitlisted, alt_alr_bok_wait
  new_waitlist = "[New Waitlist] "
  new_booking = "[New Booking] "
  hour_list = ['6:00 am','8:00 am','9:00 am','5:00 pm','6:00 pm','7:00 pm']
  day_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
  if day[:3].lower() not in day_list and time.lower() not in hour_list:
    print(f'Sorry, correct values are {day_list}/{hour_list}')
  else:
    for _ in c_list:
      if day[:3].lower() in _[0].lower() and time.upper() in _[0].upper():
        if _[1].text.lower() == "booked":
          print(f'Already {_[0]}')
        elif _[1].text.lower() == "waitlisted":
          print(f'Already on Waitlist => {_[0].replace('Booked:','')}')
          alt_alr_bok_wait+=1
        elif _[1].text.lower() == "join waitlist":
          _[1].click() # second value in tuple is button object (Selenium)
          print(f'Joined waitlist for: {_[0].replace('Booked:','')}')
          new_waitlist = "".join([new_waitlist, _[0].replace('Booked: ','')])
          waitlisted+=1
        else:
          print(f'{_[0]}')
          new_booking = "".join([new_booking,_[0].replace('Booked: ', '')])
          booked+=1
    check_bookings()
    already_booked_waitlisted = booked_dict["_counter_"]
    print("\n--- BOOKING SUMMARY ---")
    print(f'New bookings: {booked}')
    print(f'New waitlist entries: {waitlisted}')
    print(f'Already booked/waitlisted: {int(already_booked_waitlisted + alt_alr_bok_wait)}')
    print(f'Total Tuesday & Thursday 6pm classes: {already_booked_waitlisted}')
    print("\n--- DETAILED CLASS LIST ---")
    print(new_booking) if len(new_booking) > 15 else print("-booking-none-")
    print(new_waitlist) if len(new_waitlist) > 15 else print("-waitlisting-none-")

login()
again = ""
while again != "exit":
  new_whole_class()
  day = input("<at while> Type day\n")
  time = input("<at while> Type hour\n")
  choose_class(class_list,day,time)
  again = input("Add next training unit ? (`yes` - continue / `exit` - exit\n")
  if again == "exit":
    driver.quit()
    continue
