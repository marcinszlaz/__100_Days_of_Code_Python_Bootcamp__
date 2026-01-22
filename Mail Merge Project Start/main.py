import os

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".



with open('./Input/Names/invited_names.txt') as names:
  for name in names.readlines():
    letter = open('./Input/Letters/starting_letter.txt', mode = 'r')
    modifying_letter = letter.read().replace('[name]', name.strip())
    path_and_name = f"./Output/ReadyToSend/letter_for_{name.strip().replace(' ','_')}.txt"
    save_letter = open(path_and_name, mode = 'w')
    save_letter.write(modifying_letter)

letter.close() # we need to close opened letter template


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp