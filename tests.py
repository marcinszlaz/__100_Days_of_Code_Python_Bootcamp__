import os,pathlib


here = pathlib.Path.cwd()
_list = os.listdir()

print(here,_list)


def multiplying(x,y):
  return x*y

print(multiplying(2,2))

lbd_multiplying = lambda x,y:x*y

print(lbd_multiplying(2,2))

sequence = lambda seq1,seq2: [x for x in seq1 if x in seq2]
print(*sequence([1,2,3],[2,5,6]))

tuple_list = [('a','b'),('c','d'),('e','f')] # list of tuple is correct too
print(tuple_list[0][0])
print(tuple_list[2][1])

capital_case = "Soup is good on Monday at morning"
print(capital_case.lower())

with open(__file__,mode='r') as file:
  print_this = file.read()
  print(print_this)

# input("zupa jest dobra")

day = "Monday"
print(day[:3])
_ = ["Booked: cycki"]
new_booking='lubie'

print(" ".join([new_booking,f'{_[0].replace('Booked: ', '')}']))

test_dict = {"_counter_":0}
test_dict["ct1"]={"name":"bok1","counter":1}
test_dict["ct2"]={"name":"wait1"}

print(test_dict.get("ct1",{}).get("counter",0))
print(test_dict.get("ct2",{}).get("counter",0))
print('kombinacja',test_dict["ct1"].get("counter"))
print(test_dict["_counter_"])
zzz = test_dict["_counter_"]=(int(test_dict["ct1"].get("counter",0))+int(test_dict["ct2"].get("counter",0)))
print(zzz)