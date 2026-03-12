import json,pprint

href_list=[]
with open(file='./dict.json', mode='r') as f:
  object_json = json.load(fp=f)
  for _ in range(0,len(object_json)):
    try:
        print(_,' : ',object_json[_]['tracks']['items'][0]['external_urls']['spotify'])
        href_list.append(object_json[_]['tracks']['items'][0]['external_urls']['spotify'])
    except IndexError as ie:
      print(f'{_} : URL probably doesn\'t exist {ie}')
    except Exception as ex:
      print(f'Something else went wrong: {ex}')
    else:
        pass
    finally:
        pass
        # closing file f.close() and _+=1 is pointless, cos of Python iterator
        # object, this iteral can't change _ value
        # else and finally are pointless here too, but I like syntax order xD














