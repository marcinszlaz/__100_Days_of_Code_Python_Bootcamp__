import random

rezultat = ''

def string_concat(*chunks, sep = ' | ', end = '\n' ):
  """sep = separator
     end = endline
     *chunks = single or multiple string args """
  # global main.napis
  data = []
  data_list = []
  data.append(chunks)
  data_list.append([item for item in data[0]])
  result = sep.join(data_list[0])+end
  result2 = sep.join(chunks)+end # join() can handle with tuple too, comprehension list isn't needed
  return result

a=''
b=''
c=''
if (a == '' or b == '' or c == ''):
   is_empty = False
is_empty_2 = (a == '' or b == '' or c == '')
print(is_empty)
print(is_empty_2)

#Password Generator Project
def password_generator():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  # for char in range(nr_letters):
  #   password_list.append(random.choice(letters))

  password_list.extend(random.choice(letters) for _ in range(nr_letters))
  # z append wywala blad, bo append chce liste a tutaj TWORZYSZ generator (random.choice(letters) for _ in range(nr_letters))
  # ze nei moze laczyc generatora z str bo w istocie (for _ in range(1,2)) to wlasnie generator a np to samo ale w []
  # to juz lista, join,extend lubia generatory i przyjmuja je jako argument ale np random.shuffle() musi miec liste
  # nie generator

  # for char in range(nr_symbols):
  #   password_list += random.choice(symbols)

  password_list += [random.choice(symbols) for _ in range(nr_symbols)]
  # to też jak extend += to co jest rowna sie temu co jest + nastepny symbol
  # python tworzy w pamieci liste tymczasowa a potem dodaje ja do listy password_list
  # z nawiasami nie byloby listy tymczasowej w pamieci, tylko generator, ktory wrzucalby kazdy wylosowany
  # element bezposrednio do password_list, przy dużej ilosci danych w liscie tymczasowej spora oszczednosc pamieci

  # for char in range(nr_numbers):
  #   password_list += random.choice(numbers)

  password_list.extend(random.choice(numbers) for _ in range(nr_numbers))
  # to samo co wyżej ale nie dodaje całej listy i nie trzyma jej w pamięci, tylko oczko po oczku
  # bezposredni wtrysk danych z generatora xD

  random.shuffle(password_list)

  # password = ""
  # for char in password_list:
  # password += char
  # password += ''.join(char for char in password_list)
  # password=password.join(password_list)

  password = ''.join(password_list)

  # print(f"Your password is: {password}")
  # print('lista',password_list)
  napis = password
  return password



