# udoskonalanie try/except/else/finally/raise
# na podstawie programu nato alfabet
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
# print(data)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# #Opcja z WHILE
# game_on = True
# while game_on:
#   word = input("Enter a word: ").upper()
#   try:
#     output_list = [phonetic_dict[letter] for letter in word]
#   except KeyError:
#     print('Sorry, only letter in the alphabet please.')
#   else:
#     print(output_list)
#     game_on = False

# Opcja z rekurencyjnym wywołaniem funkcji xD
def nato_alphabet():
  word = input("Enter a word: ").upper()
  try:
    output_list = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print('Sorry, only letter in the alphabet please.')
    nato_alphabet()
  else:
    print(output_list)

nato_alphabet()