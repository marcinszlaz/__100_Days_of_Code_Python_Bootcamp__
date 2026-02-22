import requests
import datetime as dt

PIXELA_ENDPOINT="https://pixe.la/v1/users"
GRAPH_ENDPOINT="https://pixe.la"
USER="analnypredator6969"
TOKEN="asdbszxcvxcfaswejdsf"


user_params = {
  "token": TOKEN,
  "username": USER,
  "notMinor": "yes",
  "agreeTermsOfService": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs"
print(graph_endpoint)
graph_config = {
  "id": "graph2",
  "name": "Cycling Graph",
  "unit": "Km",
  "type": "float",
  "color": "ajisai" #purple in japan :)
  }
headers = {
  "X-USER-TOKEN":f'{TOKEN}'
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.json())

graph_endpoint_id = f"{graph_endpoint}/graph2"
headers1 = {
  "X-USER-TOKEN":TOKEN
}
today = dt.datetime.now().strftime('%Y%m%d')
print(today)
pixel_config = {
  "date":today,
  "quantity":"2.5", # before was 20.5 xd
}
# resp = requests.post(url=graph_endpoint_id,headers=headers1,json=pixel_config)
# print(resp.text)

graph_endpoint_id_put = f"{graph_endpoint}/graph2/{today}"
resp1 = requests.delete(url=graph_endpoint_id_put,headers=headers1,json=pixel_config) # .put after delete
