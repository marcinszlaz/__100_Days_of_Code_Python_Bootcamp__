import json
import os
import requests
import time as t

class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.request_data()

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

    def put_data_series(self,iata_list: list):
        """putting data series into sheet based on id from local file"""
        id_list = self.get_ids()
        ia_id = 0
        for id in id_list:
            headers = {
                "Authorization": f'Basic {os.getenv('SH_AUTH_HEADER')}',
                "Content-Type":"application/json",
            }
            body = {
                "price":{
                "iataCode":iata_list[ia_id],

                }
            }
            ia_id += 1
            response = requests.put(url=f'{os.getenv('SH_BASE_URL')}/{id}', headers=headers,json=body)
            t.sleep(0.3)
