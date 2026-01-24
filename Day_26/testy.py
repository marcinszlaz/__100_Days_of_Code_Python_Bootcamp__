import random

# LIST COMPREHENSION

numbers = [1,2,3]
new_list = []
for n in numbers:
  print(n)
  new_list.append(n)
print("new_list = ",new_list)

list = [3,2,1]
new_list = [item for item in list]
print("new_ist =",new_list)

range_list = [ran * 2 for ran in range(1,5)]
print("range_list",range_list)

## LIST COMPREHENSION WITH CONDITION(S)

name_list = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
long_cap_names = [name.upper() for name in name_list if len(name) > 5]
print("long_cap_names:",long_cap_names)

# students_score = {f"{key}":f"{random.randint(1,100)}" for key in name_list}
students_score = {key:random.randint(1,100) for key in name_list}
print("wyniki studentow",students_score)
# passed_students = {key:students_score.get(key) for key in students_score if students_score.get(key) > 60}
# get() function is equal students_score[key] but much more safer, cos it handles keys without values, returns None
# passed_students = {key:students_score[key] for key in students_score if students_score[key] >= 60} # this is mine xD
passed_students = {key:value for (key, value) in students_score.items() if value >= 60}

print("lista studentow ktorzy zdali",passed_students)

import pandas
dict_with_nested_list_as_key_value_xD = {"student":["angela", "James", "Lily"], "score": [56, 76, 98]}
student_data_frame = pandas.DataFrame(dict_with_nested_list_as_key_value_xD)
print(student_data_frame)
for (index,row) in student_data_frame.iterrows():
  # print(index)
  # print(row)
  if row.student == "James":
    print('wyniki Dżejmsa: ',row.score)