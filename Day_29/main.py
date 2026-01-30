import tkinter as tk
import tkinter.messagebox
from tkinter import Canvas, PhotoImage
import testy as ts
import random
import pyperclip

YELLOW = '#f7f5dd'
PANTEON = '#C9B27C'
PINK = '#e2979c'
GREEN = '#9bdeac'
COS = '#F0F7D4'
FONT = ('Courier',12,'bold')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
  global napis
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
  passw_entry.delete(0,tk.END)
  passw_entry.insert(0, password)
  pyperclip.copy(password) # to gunwno xD kopiuje do clipborda haslo :)
  return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
  end_string = ts.string_concat(web_entry.get(), email_user_entry.get(), passw_entry.get())
  is_ok = tkinter.messagebox.askokcancel(title='Question',message=f'{web_entry.get()}\\{passw_entry.get()}\\{email_user_entry.get()} Are above date correct ?')
  # end_string = ' | '.join(' zzz')+'\n' tak byloby najszybciej xD a tak to sie tylko bawie i bawie :)
  if (web_entry.get() == '' or email_user_entry.get() == '' or passw_entry.get() == ''):
    tkinter.messagebox.showerror(title='Ooops !',message ='Please don\'t leave any fields empty!',icon='warning')
  elif is_ok:
    with open('results.txt','a') as file:
      file.write(end_string)
    web_entry.delete(0,tk.END)
    email_user_entry.delete(0,tk.END)
    passw_entry.delete(0,'end')
    return print('Zapisano dane do pliku results.txt')
  # tkinter.messagebox.showinfo(title ='komunikat programu', message = 'Zapisano dane do pliku results.txt', icon = 'warning')



# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Password Generator')
window.config(padx=50, pady = 50, bg=PANTEON) # width i height nic nie wnosza
# dostosowanie nastepuje do rozmiaru canvas, sterujesz padx/pady

#Labels
website_lab = tk.Label(text='Website:', bg =PANTEON, font=FONT)
website_lab.grid(column = 0, row = 4, sticky ='w')
email_user_lab = tk.Label(text='Email/Username:', bg =PANTEON, font=FONT)
email_user_lab.grid(column = 0, row = 5, sticky ='w')
passw_lab = tk.Label(text='Password:', bg =PANTEON, font=FONT)
passw_lab.grid(column = 0, row = 6, sticky ='w')

#buttons
add_button = tk.Button(text = 'Add', width = 36, bg = COS,command = add_data)
add_button.grid(column = 1, row = 7)
generate_button = tk.Button(text='Generate Password:', bg = COS, command = password_generator)
generate_button.grid(column = 2, row = 6)
copy_button = tk.Button()

#Entrypoints
web_entry = tk.Entry(width = 60)
web_entry.grid(column = 1, row = 4, columnspan = 2, sticky ='w')
web_entry.focus()
web_entry.insert(tk.END,'www.ins...') # END to stała z biblioteki tkinter, 0 początek, end koniec

email_user_entry = tk.Entry(width = 60)
email_user_entry.grid(column = 1, row = 5, columnspan = 2, sticky ='w')
email_user_entry.insert(0,string = 'jankowalski@gmail.com')

passw_entry = tk.Entry(width = 42)
passw_entry.grid(column = 1, row = 6, sticky ='w')
passw_entry.insert(0,'Twoje tajne haslo')


# canvas
canvas = Canvas(width=200,height=224, bg=PANTEON, highlightthickness=0)
tomato_img = PhotoImage(file='logo.png')
canvas.create_image(100,112,image=tomato_img)
canvas.grid(column = 1, row = 0)


window.mainloop()
