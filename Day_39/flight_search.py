import requests,os
import json

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self,token):
        self.auth_token = token

    def get_iata_data(self):
        """fetching iata codes order by cities"""
        headers = {
            #"Content-Type": "application/vnd.amadeus+json",
            "Authorization": f'Bearer {self.auth_token}',
        }
        body = {
            "countryCode":"FR",
            "keyword":"PARIS",
            "max":1,
            #"include":"Airports"
        }
        response = requests.get(os.getenv('GET_IATA_URL'), headers=headers, params=body)
        r_j = response.json()
        with open(file='iata_data.json',mode='w') as file:
            json.dump(obj=r_j,fp=file, sort_keys=True,indent=2)

    def get_fl_of_search(self):
        headers = {
            # "Content-Type": "application/vnd.amadeus+json",
            "Authorization": f'Bearer {self.auth_token}',
        }
        body = {
            "originLocationCode": "WAW",
            "destinationLocationCode": "PAR",
            "adults": 1,
            "departureDate":"2026-03-20",
            "max":3,
        }
        response = requests.get(os.getenv('FLIGHT_OFFER_SEARCH_URL'), headers=headers, params=body)
        r_j = response.json()
        with open(file='flight_offer_data.json', mode='w') as file:
            json.dump(obj=r_j, fp=file, sort_keys=True, indent=2)




'''
ta klasa gada z amadeusem o lotach
'''
