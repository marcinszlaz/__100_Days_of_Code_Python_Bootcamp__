import json
import os
import requests
import time as t

class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.request_data()
        self.dict_from_lists = {}

    def request_data(self):
        """ getting data from google sheet"""
        headers = {
            "Authorization": f'Basic {os.getenv('SH_AUTH_HEADER')}',
        }
        response = requests.get(url=os.getenv('SH_BASE_URL'), headers=headers)
        r_j = response.json()
        with open(file='sheet.json',mode='w') as f:
            json.dump(obj=r_j,fp=f,indent=2,sort_keys=True)

    def post_data(self):
        """posting data into sheet"""
        headers = {
            "Authorization": f'Basic {os.getenv('SH_AUTH_HEADER')}',
            "Content-Type":"application/json",
        }
        body = {
            "price":{
            "iataCode":"petunia",

            }
        }
        response = requests.post(url=os.getenv('SH_BASE_URL'), headers=headers,json=body)

    def put_data(self):
        """putting data into sheet"""
        headers = {
            "Authorization": f'Basic {os.getenv('SH_AUTH_HEADER')}',
            "Content-Type":"application/json",
        }
        body = {
            "price":{
            "iataCode":"tests",

            }
        }
        response = requests.put(url=f'{os.getenv('SH_BASE_URL')}/2', headers=headers,json=body)

    def get_prices(self):
        """returns prices list from google sheet"""
        with open('sheet.json',mode='r') as f:
            r_f = f.read()
            js = json.loads(r_f)
            prices_list = [row['lowestPrice'] for row in js['prices']]
            return prices_list

    def get_ids(self):
        """returns ids list from google sheet"""
        with open('sheet.json',mode='r') as f:
            r_f = f.read()
            js = json.loads(r_f)
            id_list = [row['id'] for row in js['prices']]
            return id_list

    def get_cities(self):
        """returns cities list from google sheet"""
        with open('sheet.json',mode='r') as f:
            r_f = f.read()
            js = json.loads(r_f)
            cities_list = [row['city'] for row in js['prices']]
            return cities_list

    def put_data_series(self, what: str,data_list: list):
        """ - putting data series into sheet based on id from local file
            - str: name of column  which you need to update
            - data_list: list of values
            - default column's names iataCode,City,lowestPrice,cityLocCode """
        id_list = self.get_ids()
        ia_id = 0
        for id in id_list:
            headers = {
                "Authorization": f'Basic {os.getenv('SH_AUTH_HEADER')}',
                "Content-Type":"application/json",
            }
            body = {
                "price":{
                f"{what}":f"{data_list[ia_id]}",

                }
            }
            ia_id += 1
            response = requests.put(url=f'{os.getenv('SH_BASE_URL')}/{id}', headers=headers,json=body)
            t.sleep(0.3)

    def make_a_dict(self):
        """ make dict from two list, same lenght [0]-> key [0]->value
        city and price from local file """
        list_one = self.get_cities()
        list_two = self.get_prices()
        if len(list_one) == len(list_two):
            for _ in range(len(list_one)):
                self.dict_from_lists[list_one[_]]=list_two[_]
        else:
            print('lists lengths aren\'t equal !')
        return self.dict_from_lists

    def make_flights_dict(self):
        """make a compact dictionary from flights data"""
        with open('ch_f_v4.json', mode='r') as f:
            data = json.load(fp=f)
            city = data[0]['airports'][0]['arrival'][0]['airport']['name']
            price = data[0]['other_flights'][0]['price']
            dep_airport = data[0]['other_flights'][0]['flights'][0]['departure_airport']['name']
            dep_code = data[0]['other_flights'][0]['flights'][0]['departure_airport']['id']
            departure_date = data[0]['other_flights'][0]['flights'][0]['departure_airport']['time']
            arrival_airport = data[0]['other_flights'][0]['flights'][0]['arrival_airport']['name']
            arr_code = data[0]['other_flights'][0]['flights'][0]['arrival_airport']['id']
            arrival_time = data[0]['other_flights'][0]['flights'][0]['arrival_airport']['time']

            dictionary = {
                f'{city}': {
                    "price": f'{price}',
                    "depAirport": f'{dep_airport}',
                    "depCode": f'{dep_code}',
                    "depDate": f'{departure_date}',
                    "arrAirport": f'{arrival_airport}',
                    "arrCode": f'{arr_code}',
                    "arrTime": f'{arrival_time}'
                }
            }
        return dictionary
