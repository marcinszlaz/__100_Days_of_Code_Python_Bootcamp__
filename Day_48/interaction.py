from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import random as r, time as t
from selenium.webdriver.common.keys import Keys # you can use keys on www with this black magic library

URL="https://en.wikipedia.org/wiki/Main_Page"

# chrome doesn't close immediately with this option
chrome_options: Options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("--start-maximized")

driver: WebDriver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

articles = driver.find_element(By.CSS_SELECTOR, value="a[title='Special:Statistics']")
print(articles.text)

statistics = driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(statistics.text)
# statistics.click() # push the link on site :)

search1 = driver.find_element(By.NAME, value='search')
search1.send_keys("Python")
search1.send_keys(Keys.ENTER)

# search1.send_keys("Python")
# t.sleep(r.uniform(0.5,1.5))
# driver.close()
