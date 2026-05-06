import os,pathlib
from dotenv import load_dotenv
import json

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path = dotenv_path)

basedir = pathlib.Path.cwd()
print('basedir: ',basedir)
basedir_ = pathlib.Path.cwd() / 'zupa.txt'
print('basedir_: ',basedir_)
_basedir_ = 'sqlite:///' + os.getcwd() + 'movie.db'
print('_basedir_: ',_basedir_)

import requests
#  "mirror address"
URL = "https://httpbin.org/headers"

# defined headers
my_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
}
# sending requests
response = requests.get(URL, headers=my_headers)
# server response
print('simply response',response.json())

# simply way to check what looks like your header
from requests import Request, Session
s = Session()
req = Request('GET', URL, headers=my_headers)
prepped = req.prepare()
# here you have your headers
print('what I\'ll send: ',prepped.headers)

# region API requests section
def movie_searcher(params: str = "")->tuple:
    """" function gets str parameter (film name)
         and return tuple with two values
         1)dictionary (json)
         2) same content but nice formatted string          """
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Authorization":f"Bearer {os.getenv("BEARER")}"
    }
    parameters = {
        "query":f"{params}"
    }
    response = requests.get(url=os.getenv('API_URL'),headers=headers,params=parameters)
    formatted_dict = json.dumps(response.json(),indent=4,sort_keys=True)
    return response.json(),formatted_dict
# endregion

# movie_dict = movie_searcher("Good Father")
# print(movie_dict[1])
# movie_dict[0]['results'][0]["original_title"]
# movies = movie_dict[0]['results']
# for movie in movies:
#     id_ = (movie["id"])
#     original_title = (movie["original_title"])
#     release_date = (movie["release_date"])
#     img_prefix = os.getenv("IMG_PREF")
#     poster_path = f"{img_prefix}/{movie.get('poster_path')}"
#     overview = (movie["overview"])
#     print(f"{id_}: {original_title} - {release_date[:4]} - {poster_path}")

def movie_searcher_by_id(movie_id: int)->tuple:
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Authorization": f"Bearer {os.getenv("BEARER")}"
  }
  URL=f"{os.getenv('DET_URL')}{movie_id}"
  response = requests.get(url=URL, headers=headers, )
  formatted_dict = json.dumps(response.json(), indent=4, sort_keys=True)
  return response.json(), formatted_dict


mov = movie_searcher_by_id(603)

print(mov[0]['original_title'])
print(mov[0]['release_date'])
print(mov[0]['overview'])
print(mov[0]['poster_path'])

