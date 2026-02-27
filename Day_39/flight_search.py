# TODO
# 1. send cities list into amadeus, get iata codes, put iata codes on prices sheet DONE
# 2. next

import requests,os
import json

class FlightSearch:
    """This class is responsible for talking to the AMADEUS flightSearch API."""
    def __init__(self,token):
        self.auth_token = token
        self.iata_list = []
        self.data_dict = {}
        self.data_list=[]

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

    def get_fl_of_search(self):
        """ get flight offer search, we don't use this function"""
        headers = {
            # "Content-Type": "application/vnd.amadeus+json", it is needed in post/put when you send data in body,not in get func
            "Authorization": f'Bearer {self.auth_token}',
        }
        body = {
            "originLocationCode": "WAW",
            "destinationLocationCode": "PAR",
            "adults": 1,
            "departureDate":"2026-03-20",
            "max":1,
        }
        response = requests.get(os.getenv('FLIGHT_OFFER_SEARCH_URL'), headers=headers, params=body)
        r_j = response.json()
        with open(file='flight_offer_data.json', mode='w') as file:
            json.dump(obj=r_j, fp=file, sort_keys=True, indent=2)

    def get_cheapest_flights(self):
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


