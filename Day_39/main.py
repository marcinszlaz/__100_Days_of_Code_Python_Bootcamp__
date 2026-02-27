#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# google sheet data management -> https://sheety.co/

# flight search api, free account needed -> https://developers.amadeus.com/
# another amadeus url (docs) -> https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference
# amadeus api and tokens howto -> https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335
# amadeus airports codes by city -> https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference

# sms management twilio -> https://www.twilio.com/docs/messaging/quickstart/python

import requests
import pathlib,os
from dotenv import load_dotenv
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import json

import flight_data as fd
import flight_search as fs
import data_manager as dm

# fetching token
# amadeus has oauth2 type of authorization
# https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#third-recommended-define-automatic-token-refresh-and-update  --> url with documentation

token = fd.FlightData() # validating and getting token
f_dest = fs.FlightSearch(token.token)
# f_dest.get_fl_of_search()
f_s = dm.DataManager() # constructor gets data from google sheet
# f_s.put_data_series(f_dest.get_iata_codes(city_list=f_s.get_cities())) # updating iata codes on google sheet
f_dest.get_cheapest_flights()
