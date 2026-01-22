# LIST COMPREHENSION

numbers = [1,2,3]
new_list = []
for n in numbers:
  print(n)
  new_list.append(n)
print('new_list = ',new_list)

list = [3,2,1]
new_list = [item for item in list]
print('new_ist =',new_list)

range_list = [ran * 2 for ran in range(1,5)]
print('range_list',range_list)

## LIST COMPREHENSION WITH CONDITION(S)

name_list = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
long_cap_names = [name.upper() for name in name_list if len(name) > 5]
print('long_cap_names:',long_cap_names)

