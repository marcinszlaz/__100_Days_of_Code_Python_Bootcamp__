import requests,pprint
from bs4 import BeautifulSoup
import notification_manager as nm

PRICE = 100
TEST_URL = "https://appbrewery.github.io/instant_pot/"
result = requests.get(url="https://appbrewery.github.io/instant_pot/")

sp = BeautifulSoup(markup=result.text,features="html.parser")
# Fetching price method one
whole_price = sp.select("#corePrice_feature_div > div > div > span.a-price.aok-align-center > span:nth-child(2) > span.a-price-whole")
fraction_price = sp.select("#corePrice_feature_div > div > div > span.a-price.aok-align-center > span:nth-child(2) > span.a-price-fraction")
full_price = float(whole_price[0].get_text().replace(".","")+'.'+fraction_price[0].get_text())

# Fetching price
# method two, much simplier but I don't know where site part with this class
# Chrome, F12, console, inspect(document.querySelector('.searched-class'))
# right mouse button, scroll into view :-)
price = sp.find(class_="a-offscreen").get_text().split("$")[1]
float_price = float(price)

# fetching title
product_title_dirty = sp.select("span#productTitle.a-size-large.product-title-word-break")
product_title_clean = " ".join((product_title_dirty[0].get_text().split()))

# fetching url to instant store
url_to_store_dirty = sp.select("a#bylineInfo")
url_to_store_clear = url_to_store_dirty[0].get('href')

# building message
msg = f"{product_title_clean} is now ONLY: ${float_price}, you can buy it at: {url_to_store_clear}"

send = nm.NotificationManager()
if float_price < PRICE:
  print('We got a bargain !')
  send.send_email(subject="We got a bargain !", message=msg)

