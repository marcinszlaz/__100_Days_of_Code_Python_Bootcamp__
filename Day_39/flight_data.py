import pathlib,os
from dotenv import load_dotenv
from oauthlib.oauth2 import BackendApplicationClient
from pandas.io.formats.format import return_docstring #hmm, to później chyba xD
from requests_oauthlib import OAuth2Session
import json, datetime as dt
from zoneinfo import ZoneInfo

class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self):
        self.token = None
        self.load_env()
        self.file_mod_time_unix = dt.datetime.now().timestamp()
        self.file_path = pathlib.Path.cwd() / 'auth_data.json'
        self.token_checker()

    def return_token_from_file(self,mode='r'):
        with open(file=self.file_path,mode=mode) as file:
            data = json.load(file)
            self.token = data['access_token']
            return data

    def load_env(self):
        """environment values loading"""
        path = pathlib.Path.cwd() / '.env'
        load_dotenv(dotenv_path=path)

    def token_checker(self):
        """ check token presence on the board"""
        file_path = pathlib.Path.cwd() / 'auth_data.json'
        is_file_exist = pathlib.Path.is_file(pathlib.Path.cwd() / 'auth_data.json')
        if is_file_exist:
            self.file_mod_time_unix = os.path.getmtime(file_path)
        file_mod_time_iso = dt.datetime.fromtimestamp(timestamp=self.file_mod_time_unix, tz=ZoneInfo('Europe/Warsaw'))
        time_now = dt.datetime.now(tz=ZoneInfo('Europe/Warsaw'))
        if is_file_exist:
            print('token file exists')
            if (time_now - file_mod_time_iso) > dt.timedelta(minutes=29):
                print('token expired, generate new one')
                self.fetch_token_()
                return self.return_token_from_file()
            else:
                print('token is valid, you can get token by variable .token')
                return self.return_token_from_file()
        else:
            print('file doesn\'t exist, generate new file')
            self.fetch_token_()
            return self.return_token_from_file()

    def fetch_token_(self):
        """fetching token from amadeus"""
        client_id = os.getenv('AMD_APIKEY')
        client_secret = os.getenv('AMD_APISECRET')
        client = BackendApplicationClient(client_id=client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url=f'{os.getenv('AMD_BASE_URL_GET_TOKEN')}', client_id=client_id,
                                  client_secret=client_secret)
        with open('auth_data.json', mode='w') as file:
            json.dump(obj=token, fp=file, sort_keys=True,indent=4)
