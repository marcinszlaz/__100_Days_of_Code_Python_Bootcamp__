payload = {
    "can_take_calls": "0",
    "coffee_price": "10.5",
    "has_sockets": "0",
    "has_toilet": "0",
    "has_wifi": "0",
    "img_url": "CYCKI",
    "location": "LUBIE_2",
    "map_url": "CYCKI",
    "name": "LUBIE_2",
    "seats": "cycki"
  }
values_to_change = {"0": False,"": False," ": False,"False": False, "false": False, "1": True,"true": True,"True": True}
new_new = {k:(values_to_change[v] if v in values_to_change else v)  for k,v in payload.items()}
new_new_new = {k:(values_to_change.get(v,v)) for k,v in payload.items()}
new_payload = {}
for k,v in payload.items():
  if v not in values_to_change.keys():
    new_payload[k] = v
  elif v in values_to_change.keys():
    v = values_to_change[v]
    new_payload[k] = v
  else:
    v = None
    new_payload[k] = v

print(new_payload)
print(new_new)
print(new_new_new)
