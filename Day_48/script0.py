import time as t
from selenium.webdriver.common.by import By
from selenium import webdriver

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# Open Chrome browser
PRODUCTION_URL="https://www.amazon.pl/Instant-Pot-Duo-Autocuiseur-Multifonction/dp/B08Z4HCGDH/ref=sr_1_5?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-5"
PYTHON_URL="https://www.python.org/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(PYTHON_URL)

# price_dollar = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# print(f'The price is {price_dollar.text}.{price_cents.text}')

# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar)
# documentation_link = driver.find_element(By.CSS_SELECTOR,value='.documentation-widget a') # div class and anchor deep inside no directly under div, selenium handles this with putting low effort xD
# print(documentation_link.text)

# searching by X-PATH
bug_link = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close() # closes one tab
driver.quit() # close whole browser
