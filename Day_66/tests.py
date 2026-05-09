# USE CURL instead of POSTMAN :)
# curl http://127.0.0.1:5000/add -X POST -d "name=LUBIE&map_url=CYCKI&img_url=CYCKI&location=CYCKI&seats=cycki&has_toilet=True&has_wifi=True&has_sockets=True&can_take_calls=True&coffee_price=duzo"

'''

curl http://127.0.0.1:5000/add -X POST -d "{'name'='LUBIE1','map_url'='CYCKI','img_url'='CYCKI','location'='CYCKI','seats'='cycki','has_toilet'=1,'has_wifi'=,&'has_sockets'=1,'can_take_calls'=1,'coffee_price'=duzo}"

curl -X POST -H "Content-Type: application/json" -d '{"name":"LUBIE1","map_url":"CYCKI","img_url":"CYCKI","location":"CYCKI","seats":"cycki","has_toilet":true,"has_wifi":true,"has_sockets":true,"can_take_calls":true,"coffee_price":duzo}' http://127.0.0.1:5000/add

'''

import random as r

list_one = [1,2,3,4]

print(list_one)
new_list = r.shuffle(list_one)
print(list_one)
print(r.choice(list_one))
cho = r.choice(list_one)
print(cho)

big_dict = {
  "can_take_calls": "True",
  "coffee_price": "duzo",
  "has_sockets": "True",
  "has_toilet": "True",
  "has_wifi": "True",
  "img_url": "CYCKI",
  "location": "CYCKI",
  "map_url": "CYCKI",
  "name": "LUBIE",
  "seats": "cycki",
}

# print(big_dict)

def multi_print(**kwargs):
  print('cycki',kwargs)

multi_print(**big_dict)

'''
*** N O R M A L ***

add_normal
normal type of sending data
receiving by use request.form.get('name')

curl http://127.0.0.1:5000/add-normal -X POST -d "name=LUBIE_2&map_url=CYCKI&img_url=CYCKI&location=LUBIE_2&seats=cycki&has_toilet=&has_wifi=0&coffee_price=10.5"

if you put inside bool intended field anything it'll be true (1,0,True,False) doesn't matter, if you don't put anything it'll be false

*** J S O N ***

in JSON standard, we always use true / false NOT True / False
don't send this below, use this more below xD
this is intended for receiving by request.get_json()

curl -X POST -H "Content-Type: application/json"
-d '{"name": "Film1",
"map_url": "url_film1",
"img_url": "url_film1",
"location": "film1",
"seats": "seat_film1",
"has_toilet": true,
"has_wifi": true,
"has_sockets": true,
"can_take_calls": true,
"coffee_price": 30 }'
http://127.0.0.1:5000/add

ready to copy paste
curl -X POST -H "Content-Type: application/json"  -d '{"name": "xxx",  "map_url": "url_film1", "img_url": "url_film1",  "location": "xxx",  "seats": "seat_film1", "has_toilet": true,  "has_wifi": true,  "has_sockets": false, "can_take_calls": true, "coffee_price": 30 }' http://127.0.0.1:5000/add-json

*** D I C T I O N A R Y ***
this is intended for receiving by request.form.to_dict()
input is basically the same as with normal

I cutted bool values, with bool vaulues when you receive it by to_dict()
is that problem, Python doesn't know how to interprets it

curl http://127.0.0.1:5000/add-dict -X POST -d "name=LUBIE_3&map_url=CYCKI&img_url=CYCKI&location=LUBIE_3&seats=cycki&has_toilet=0&has_wifi=0&can_take_calls=0&has_sockets=0&coffee_price=10.5"


*** P A T C H ***
curl http://127.0.0.1:5000/update-price/29?price=3000

*** D E L E T E ***
curl http://127.0.0.1:5000/report-closed/30?api_key=TopSecretAPIKey

### generate documentation ###
!!!you can create nice docs of your API using POSTMAN!!!
POSTMAN is free
https://documenter.getpostman.com/view/54629649/2sBXqNmJPd
'''