from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

URL="https://www.python.org/"

# chrome doesn't close immediately with this option
chrome_options: Options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver: WebDriver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

print('title',driver.title)
print('browser name',driver.name)
# driver.save_screenshot(filename='www_photo.png') # Mommy, Mommy I did screenshot !
# cutting whole div by class name from www
whole_div = driver.find_element(By.CLASS_NAME,value="medium-widget.event-widget.last")

# searching inside whole_div selenium object
mmdd = whole_div.find_elements(By.TAG_NAME, value="time")
anchor = whole_div.find_elements(By.CSS_SELECTOR,value="a:not([title])") # pseudoclass :not([]) excludes bad ones :)

www_dict ={}
if len(mmdd) == len(anchor):
  print('Arrays have equal length')
  for index,(t,a) in enumerate(zip(mmdd,anchor), start = 0):
    www_dict[index]=dict(time=t.get_attribute("datetime").split("T")[0],name=a.text)
else:
  print('Arrays have different length')

print(www_dict)

# driver.close() # close opened tab
driver.quit() # quit from browser