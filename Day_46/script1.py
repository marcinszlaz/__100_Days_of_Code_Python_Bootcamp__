import datetime as dt
import requests,time
from bs4 import BeautifulSoup
import spotipy,json
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import pathlib,os

# I commented this below, because site doesn't allow anymore checking hot 100 hits
# from the past, this option is only available for premium members
# NOPE, WE CAN STEAL IT ! xD (what we need is to change web url add date at the end)

url_addon=None
date=""
song_names=[]
artist_names=[]

path= pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=path)

# Spotify authorization with Oauth2.0 only
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"), client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"), redirect_uri=os.getenv("SPOTIFY_REDIRECT_URL"), scope="playlist-modify-public", cache_path="token.txt"))
# cache_path=".cache" creates .cache file with tokens
# without this option library does it anyway itself
# lawful scope -> "playlist-modify-private"

def get_date():
  global url_addon
  global date
  try_again = True
  while try_again:
    try:
      date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
      url_addon = str((dt.datetime.strptime(date, "%Y-%m-%d"))).split(sep=" ")[0]
    except ValueError as ve:
        print('Only format YYYY-MM-DD is allowed')
        again = input('Do you wanna try again? (y/n)')
        if again == 'y':
          try_again = True
        else:
          try_again = False
    else:
      try_again = False

def scrapper():
  """scrapping 100 top hits from https://www.billboard.com/charts/hot-100/ """
  global song_names
  global artist_names
  # you're web scrapping, so it will be better when web server thinks you're human not bot, that's why we're using our web browser header
  header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
  }
  basic_url = f"https://www.billboard.com/charts/hot-100/{url_addon}"
  # .select() it's more precise than find(_all), honestly I can't figure it  out myself  how to scrap it, and may thoughts was closer this conception li>ul>.. than simply li ul... , so I copied this solution from TheMuaellator from github xD

  response = requests.get(url=basic_url,headers=header)
  soup = BeautifulSoup(markup=response.text, features="html.parser")
  song_names_spans = soup.select("li ul li h3")
  song_names = [song.getText().strip() for song in song_names_spans]
  artist_name_spans = soup.select("li ul li span.c-label.a-no-trucate.a-font-secondary") # but this one I did myself xD
  artist_names = [artist.getText().strip() for artist in artist_name_spans]

def print_songs_artists():
  global song_names
  global artist_names
  for index, (song, artist) in enumerate(zip(song_names, artist_names), start=1):
    print(index,':',song,' - ',artist)

# we do not need this anymore, because user_playlist_create function is obsolete
# and will be removed from future spotipy library
def get_user_data():
  """fetching current spotify user data"""
  us_id = sp.current_user()
  print('user id: ',us_id['id'])
  return us_id['id']

def create_playlist(date=date):
  """creating new playlist, requires date parameter"""
  d = date
  playlist = sp.current_user_playlist_create(name=f"{d} Billboard 100",description="List of 100 best tracks from chose date",public=True,collaborative=True)
  playlist_id = playlist['id']
  return playlist_id

def get_user_playlists():
  """doesn't work xD do not use it :)"""
  sp.current_user_playlists(limit=5, offset=0)

def track_searcher(songs: list,artists: list):
  """I'm searching for tracks ! Do not bother me too often !"""
  result=[]
  if len(songs) != len(artists):
    print('Lists haven\'t equal length')
  for track,artist in zip(songs,artists):
    q=f'track:"{track}" artist:"{artist}"'
    result.append(sp.search(q=f'{q}', limit=1, type="track"))
    time.sleep(0.1)
  with open('./dict.json',mode='w') as f:
    json.dump(obj=result,fp=f,indent=2,sort_keys=True)

def url_extractor():
  href_list = []
  with open(file='./dict.json', mode='r') as f:
    object_json = json.load(fp=f)
    for _ in range(0, len(object_json)):
      try:
        print(_, ' : ', object_json[_]['tracks']['items'][0]['external_urls']['spotify'])
        href_list.append(object_json[_]['tracks']['items'][0]['external_urls']['spotify'])
      except IndexError as ie:
        print(f'{_} : URL probably doesn\'t exist {ie}')
      except Exception as ex:
        print(f'Something else went wrong: {ex}')
      else:
        pass
      finally:
        #f.close()
        #_+=1
        pass
        # closing file f.close() is pointless, cos file is closed
        # after line 101 by with(), and _+=1 is pointless too cos of Python
        # iterator object, this iteral can't change _ value
        # else and finally are pointless here too, but I like syntax order xD
  return href_list

def add_tracks_to_playlist():
  """ call for two functions and gets both as an arguments"""
  id_ = create_playlist()
  items_ = url_extractor()
  sp.playlist_add_items(playlist_id=id_,items=items_) # items expects list of urls

# url = search_tracks_tests(tracks="Żul w swetrze",artists="Sneaky Jesus")
# print(url)
# get_user_data()
# create_playlist(date)

get_date()
scrapper()
print_songs_artists()
get_user_data()
track_searcher(song_names,artist_names)
add_tracks_to_playlist()