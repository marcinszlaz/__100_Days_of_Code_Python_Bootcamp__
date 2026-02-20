import sms
import requests as r
import json as j
import datetime as dt
from dotenv import load_dotenv
import os, pathlib, html as h
from newsapi.newsapi_client import NewsApiClient
import textwrap as txw

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MSG = ''

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TIME SECTION xD
today = dt.date.today()
yesterday = today - (dt.timedelta(days=1))
the_day_before_yrd = today - dt.timedelta(days=2)

# FETCHING AND SAVING BUSINESS DATA
path_data_file = pathlib.Path.cwd() / 'alphavantage_data1.json'
if not os.path.isfile(path_data_file): # if file with data not exists we fetch data from API
  path_env = pathlib.Path.cwd() / '.env'
  load_dotenv(dotenv_path=path_env)
  # parameters dict for url API request
  parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":f'{STOCK}',
    "interval":'60min',
    "apikey":f'{os.getenv('ALFA_API')}',
    "datatype":"json"
  }
  alphavantage_connector = r.get(url="https://www.alphavantage.co/query?",params=parameters)
  alphavantage_data_as_js_object = alphavantage_connector.json() # json obj
  alphavantage_data_as_str = j.dumps(alphavantage_data_as_js_object, indent=4, sort_keys=True) # str obj
  # save data to file#1
  with open(file='alphavantage_data.json', mode='w') as file:
    file.write(alphavantage_data_as_str) # file.write() expects string returns str likelihood dict
  # save data to file#2
  with open(file='alphavantage_data1.json', mode='w') as file:
    j.dump(alphavantage_data_as_js_object, fp=file, indent=4, sort_keys=True)
    #  j.dump() expects json object returns dictionary
    print('Files created!')
else:
  print('Files was created before!')
  pass

with open('alphavantage_data1.json', mode='r') as file:
  data_str = file.read()
  data_json_loads = j.loads(data_str) #  j.loads(str) json DICT from str
  file.seek(0)
  data_json_load = j.load(file) # j.load(file hook) json dict from file hook,
  # j.load needs return at file beginning

# ## STEP 2: Use https://newsapi.org
# # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# FETCHING AND SAVING NEWS AND ARTICLES
path_env = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=path_env)
newsapi = NewsApiClient(api_key=f'{os.getenv('NEWS_API')}')
all_sources = newsapi.get_top_headlines(
                                          category='business', #technology,science
                                          language='en',
                                          country='us',
                                          )
source_str = ','.join([row['source']['name'] for row in all_sources['articles'][::1]]) # list (str) of media sources
all_articles = newsapi.get_everything(q='Microsoft',
                                      # sources=source_str,
                                      # domains='bbc.co.uk,techcrunch.com',
                                      from_param=the_day_before_yrd,
                                      to=today,
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
with open('articles.json',mode='w', encoding='utf-8') as file:
  j.dump(all_articles,fp=file, indent=4,sort_keys=True)
  # file.seek(0)
with open('articles.json',mode='r') as file:
  art = j.load(file)
ls_impr = [{"Title":h.unescape(row['title']), "Description":h.unescape(row['description'])} for row in art['articles'][:3]]

# COMPARING DATA
y_price = float((data_json_load['Time Series (Daily)'][f'{yesterday}']['3. low']))
by_price = float((data_json_load['Time Series (Daily)'][f"{the_day_before_yrd}"]['2. high']))
percent_diff = float(round((((y_price - by_price)/by_price)*100),2))
if percent_diff > 1.0 or percent_diff < 1.0:
  marker = '🔺' if percent_diff > 1.0 else '🔻'
  print(f'TSLA: {marker}{abs(percent_diff)}% \nHeadline:{ls_impr[0]['Title']}\nBrief: {txw.fill(ls_impr[0]['Description'],width=80)}')
  message = f'TSLA: {marker}{abs(percent_diff)}% \nHeadline:{ls_impr[0]['Title']}\nBrief: {ls_impr[0]['Description']}'
  MSG = message
sms.send_sms(MSG)

# ## STEP 3: Use https://www.twilio.com
# # Send a seperate message with the percentage change and each article's title and description to your phone number.
#
#
# #Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
#
