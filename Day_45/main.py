# PROJECT 45
# useful hints !
# ctrl shift i - inspection i chrome and other browsers
# ctrl shift c - tool for getting css selector addresses

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# step first - getting data from url
response = requests.get(url=URL)

# step second - parsing url data from requests `text` to soup object
soup = BeautifulSoup(markup=response.text,features="html.parser")
tests = soup.select(selector="h3.title")

# step third - creating list of films
film_list = []
for row in tests:
  film_list.append(" ".join((row.text).split()[1:]))

film_in_right_order = []
# print(film_list)

# film_list.sort(reverse=True)
sorted_films = sorted(film_list,reverse=True)
print(sorted_films)
for i,film in enumerate(sorted_films, start=1):
  print(i,film)

# tests2 = soup.find(name="h3")
# print(tests2)
