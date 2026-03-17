import requests,pprint
from bs4 import BeautifulSoup
import notification_manager as nm
from fake_useragent import UserAgent
import random
import time as t

# variables
PRICE = 400
TEST_URL = "https://appbrewery.github.io/instant_pot/"
PRODUCTION_URL = ["https://www.amazon.pl/Instant-Pot-Duo-Autocuiseur-Multifonction/dp/B08Z4HCGDH/ref=sr_1_5?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-5"]

ug=UserAgent()
def scrap_scrap():
  FULL_HEADER_CUTTED = {
      "Accept-Language": "pl-PL",
      "User-Agent": f"{ug.random}",
      "Referer": "https://www.google.com/",
    }
  for url in PRODUCTION_URL:
    result = requests.get(url=url,headers=FULL_HEADER_CUTTED)
    with open('./amazon_raw.html',mode='wb') as file:
      file.write(result.content) # you need wb mode, because .content gives you raw binary from web browser, or something like that :)
    with open('./amazonscrapping.html',mode='w',encoding="utf-8") as file:
      file.write(result.text)
    t.sleep(random.uniform(1, 5)) # fake delay generator, uniform generates float numbers eg. 1.54,4.33 etc.

with open('./amazon_raw.html', mode='rb') as file:
  result = file.read()

sp = BeautifulSoup(markup=result,features="html.parser")
# Fetching price method one
whole_price = sp.select("#corePrice_feature_div > div > div > div > span.a-price.aok-align-center.apex-pricetopay-value > span:nth-child(2) > span.a-price-whole")
fraction_price = sp.select("#corePrice_feature_div > div > div > div > span.a-price.aok-align-center.apex-pricetopay-value > span:nth-child(2) > span.a-price-fraction")
full_price = float(whole_price[0].get_text().replace(".","").replace(",","")+'.'+fraction_price[0].get_text())

## Fetching price
## method two, much simplier but I don't know where site part with this class
## Chrome, F12, console, inspect(document.querySelector('.searched-class'))
## right mouse button, scroll into view :-)
price = sp.find(class_="a-offscreen").get_text().replace(",",".").replace("zł","")
float_price = float(price)

## fetching title
product_title_dirty = sp.select("#productTitle")
product_title_clean = " ".join((product_title_dirty[0].get_text().split()))

## fetching url to instant store
url_to_store_dirty = sp.select("a#bylineInfo")
url_to_store_clear = url_to_store_dirty[0].get('href')

## building message
msg = f"{product_title_clean} is now ONLY: {full_price:.2f}pln, you can buy it at: {url_to_store_clear}"

send = nm.NotificationManager()
if full_price < PRICE:
  print('We got a bargain !')
  send.send_email(subject="We got a bargain !", message=msg)
