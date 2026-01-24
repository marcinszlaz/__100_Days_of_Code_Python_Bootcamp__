import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
bad_dict = {}
bad_dict1 = {}
bad_dict2 = {}
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
with open('nato_phonetic_alphabet.csv',mode='r',encoding='utf-8') as file:
    # file_content = file.read()
    df1 = pandas.read_csv(file)

# dicionary solution 1, cos index is first col, key.letter second col and key.code 3rd in `pandas nomenclature`
bad_dict = {key.letter:key.code for (index,key) in df1.iterrows()}
print('bad_dict: ',bad_dict)

# dicitonary solution 2
for (index,row) in df1.iterrows():
    # print(index, row.letter,':',row.code)
    bad_dict1[row.letter]=row.code
print('bad_dict1: ',bad_dict1)

# dictionary solution 3
bad_dict_tmp = df1.to_dict()
for _ in range(0,len(bad_dict_tmp['letter'])):
    bad_dict2[bad_dict_tmp['letter'][_]] = bad_dict_tmp['code'][_]

print('bad_dict2:',bad_dict2)

# dictionary solution 4
bad_dict3 ={bad_dict_tmp['letter'][_]:bad_dict_tmp['code'][_] for _ in range(0,len(bad_dict_tmp['letter']))\
            if len(bad_dict_tmp['letter']) == len(bad_dict_tmp['code']) }
print('bad_dict3:',bad_dict3)

user_input = input('Please type a word, for example your name ')
usr_input_list = [letter for letter in user_input]
output = {bad_dict1[letter.upper()] for letter in usr_input_list}
print(output)

