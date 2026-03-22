from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import random as r, time as t
from selenium.webdriver.common.keys import Keys # you can use keys on www with this black magic library

URL="http://secure-retreat-92358.herokuapp.com/"

# chrome doesn't close immediately with this option
chrome_options: Options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("--start-maximized")

driver: WebDriver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

first_name = driver.find_element(By.NAME,value="fName")
first_name.send_keys("Janusz")
first_name.send_keys(Keys.TAB)
last_name = driver.find_element(By.NAME,value="lName")
last_name.send_keys("Kowalsky")
last_name.send_keys(Keys.TAB)
email_address = driver.find_element(By.NAME,value="email")
email_address.send_keys("januszkowalsky@puppa.com")
sign_up = driver.find_element(By.CSS_SELECTOR,value="button.btn.btn-lg.btn-primary.btn-block")
sign_up.send_keys(Keys.ENTER)


# driver.close()
