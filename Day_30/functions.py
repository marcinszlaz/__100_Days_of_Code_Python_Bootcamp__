from random import randint, choice, shuffle

# function reponsible for concatenating *args
def string_concat(*chunks, sep = ' | ', end = '\n' ):
  result = sep.join(chunks)+end
  return result

#Password Generator Project
def password_generator():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_list = []
  password_list.extend(choice(letters) for _ in range(randint(8,10))) # generator
  password_list += [choice(symbols) for _ in range(randint(2,4))] # adding list created in memory
  password_list.extend([choice(numbers) for _ in range(randint(2,4))]) # list extended by a second list
  shuffle(password_list)
  password = ''.join(password_list)
  return password


print(password_generator())
