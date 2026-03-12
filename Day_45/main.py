# PROJECT 45
# useful hints !
# ctrl shift i - inspection i chrome and other browsers
# ctrl shift c - tool for getting css selector addresses

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# step 1st - getting data from url
response = requests.get(url=URL)

# step 2nd - parsing url data from requests `text` to soup object
soup = BeautifulSoup(markup=response.text,features="html.parser")
tests = soup.select(selector="h3.title")

# step 3rd - creating list of films
film_list = []
for row in tests:
  film_list.append(" ".join((row.text).split()[1:]))

# reversing method1
film_list.reverse()
print(film_list)
# reversing method2
film_list = film_list[::-1]
print(film_list)
# reversing method3
new_film_list=[]
for _ in range(len(film_list)-1, -1, -1):
  new_film_list.append(film_list[_])
print(new_film_list)

# step 4th - create new reversed list, tuples
new_list=[]
film_list.reverse()
for i,film in enumerate(film_list, start=1):
  # print(i,film)
  new_list.append(f'{i}) {film}')

# with open("movies.txt",mode='w') as file:
#   for row in new_list:
#     file.write(f'{row}')

with open("movies.txt",mode="w", encoding="utf-8") as file:
  for row in new_list:
    file.write(f'{row}\n')


