# TODO
# 1. send cities list into amadeus, get iata codes, put iata codes on prices sheet DONE
# 2. next

import requests,os
import json,time

class FlightSearch:
  """This class is responsible for talking to the AMADEUS flightSearch API."""
  def __init__(self,token):
    self.auth_token = token
    self.iata_list = []
    self.data_dict = {}
    self.data_list=[]
    self.price_list = []
    self.price_dict = {}
    self.kgmid_list = []
  def get_iata_data(self,city_list: list):
    """fetching iata data, order by cities, only for testing purpose"""
    with open(file='iata_data.json',mode='w') as file:
      pass
    with open(file='iata_data.json',mode='a') as file:
      for city in city_list:
        headers = {
          #"Content-Type": "application/vnd.amadeus+json",
          "Authorization": f'Bearer {self.auth_token}',
        }
        body = {
          # "countryCode":"",
          "keyword":[city], # it takes only one str keyword, list not allowed !
          "max":1,
          #"include":"Airports"
        }
        response = requests.get(os.getenv('GET_IATA_URL'), headers=headers, params=body)
        r_j = response.json().get('data')
        self.data_list.append(r_j)
        self.data_dict['cities']=self.data_list
      json.dump(obj=self.data_dict,fp=file,indent=2,sort_keys=True,separators=(',',':'))

  def get_iata_codes(self, city_list: list):
    """fetching iata codes order by cities"""
    for city in city_list:
      headers = {
        "Authorization": f'Bearer {self.auth_token}',
      }
      body = {
        # "countryCode":"",
        "keyword":[city], # it takes only one str keyword, list not allowed !
        "max":1,
        #"include":"Airports"
      }
      response = requests.get(os.getenv('GET_IATA_URL'), headers=headers, params=body)
      r_j = response.json()
      self.iata_list.append(r_j['data'][0]['iataCode'])
    return self.iata_list

  def get_iata_codes_v2(self,city_list: list):
    """ maybe this API will work properly :/"""
    for city in city_list:
      flights_parameters = {
        "engine": "google_flights_autocomplete",
        "q": f"{city}",
        # "exclude_regions": "true",
        "api_key": f"{os.getenv('SERP_API')}",
      }

      response = requests.get(url=os.getenv('GOOGLE_FLIGHTS_ENDPOINT'), params=flights_parameters)
      data = response.json()["suggestions"][0]["airports"][0]['id']
      self.iata_list.append(data)
    return self.iata_list

  def get_fl_of_search(self):
    """ get flight offer search, we don't use this function"""
    headers = {
      # "Content-Type": "application/vnd.amadeus+json", it is needed in post/put when you send data in body,not in get func
      "Authorization": f'Bearer {self.auth_token}',
    }
    body = {
      "originLocationCode": "WAW",
      "destinationLocationCode": "PAR",
      "departureDate":"2026-03-02",
      "returnDate":"2026-03-30",
      "nonStop":"true",
      "currencyCode":"GBP",
      "adults": 1,
      "max":5,
    }
    response = requests.get(os.getenv('FLIGHT_OFFER_SEARCH_URL'), headers=headers, params=body)
    r_j = response.json()
    with open(file='flight_offer_data.json', mode='w') as file:
      json.dump(obj=r_j, fp=file, sort_keys=True, indent=2)

  def get_cheapest_flights(self):
    """AMADEUS endpoint here is obsolete and no longer support
    so function is valid but return nothing """
    headers = {
      "Authorization": f'Bearer {self.auth_token}',
    }
    params = {
      "origin":"WAW",
      "destination":"PAR",
      "departureDate":"2026-03-30",
      "oneWay":"True",
      "viewBy":"DATE",
    }
    response = requests.get(url=os.getenv('AMD_CHEAP_URL'),headers=headers,params=params)
    r_j = response.json()
    with open(file='ch_fl.json',mode='w') as f:
      json.dump(obj=r_j,fp=f,indent=2,sort_keys=True)

  def get_cheapest_flights_v2(self, data_list: list):
    """based on google api"""
    with open('ch_f_v3.json', mode='w') as f:
      pass
    with open('ch_f_v3.json',mode='a') as f:
      for code in data_list:
        flights_parameters = {
          "engine": "google_flights",
          "type":1, # 1 round trip, 2 one way, 3 multicity
          "adults":1,
          # "sort_by":2, # sort by price
          "departure_id": "/m/01662y", #city of Bydgoszcz kgmid (PL)
          "arrival_id": f"{code}",
          "outbound_date": "2026-03-10",
          "return_date": "2026-03-30", # no needed if type:2, obligatory if type:1
          "currency": "EUR",
          "hl": "en",
          "api_key": f"{os.getenv('SERP_API')}",
        }
        response = requests.get(url=os.getenv('google_flights_endpoint'), params=flights_parameters)
        self.price_list.append(response.json())
        # self.price_dict["prices"] = self.price_list
      json.dump(obj=self.price_list,fp=f,indent=2,sort_keys=True,separators=(',',':'))
      time.sleep(0.1)

  def get_cheapest_flights_v4(self, from_="/m/04jpl", data_list = []):
    """based on google api verions 4 xD"""
    with open('ch_f_v4.json',mode='w') as f:
      flights_parameters = {
        "engine": "google_flights",
        "type":2, # 1 round trip, 2 one way, 3 multicity
        "adults":1,
        "sort_by":2, # sort by price
        "departure_id": f'{from_}', # London
        "arrival_id": f'{','.join(data_list)}',
        # "arrival_id": f"{data_list}",
        "outbound_date": "2026-03-05",
        # "return_date": "2026-03-30", # no needed if type:2, obligatory if type:1
        "currency": "EUR",
        "hl": "en",
        "api_key": f"{os.getenv('SERP_API')}",
      }
      response = requests.get(url=os.getenv('google_flights_endpoint'), params=flights_parameters)
      self.price_list.append(response.json())
      json.dump(obj=self.price_list,fp=f,indent=2,sort_keys=True,separators=(',',':'))

  def get_kgmid_to_file(self, city_list: list):
    """function get kgmid codes of cities (locations)"""
    cities = city_list
    for city in cities:
      params = {
        "engine": "google_flights_autocomplete",
        "q": f"{city}",
        "api_key": f"{os.getenv('SERP_API')}"
      }
      response = requests.get(url=os.getenv('GOOGLE_FLIGHTS_ENDPOINT'), params=params)
      r_j = response.json()
      self.kgmid_list.append(r_j)
      time.sleep(0.1)
    with open(file='kgmid_list.json',mode='w') as f:
      json.dump(obj=self.kgmid_list,fp=f,sort_keys=True,indent=2)

  def retrieve_kgmid_from_file(self):
    """ retrieving kgmid's from file on local disk"""
    give_me_the_disc = []
    with open('kgmid_list.json', mode='r') as f:
      file = json.load(fp=f)
      give_me_the_disc += [data['suggestions'][0]['airports'][0]['city_id'] for data in file]
    return give_me_the_disc
