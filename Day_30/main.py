# pracujemy z DŻEIJSON'em xD
# json.dump('<nazwa_pliku>',file(z with open),indent=4) funkcja zapisujaca na dysk write
# json.load(file z with open()) funkcja odczytująca read
# json.update() - updejt

import tkinter as tk
import tkinter.messagebox
from tkinter import Canvas, PhotoImage
import functions as ts
from random import randint, choice, shuffle
import pyperclip
import json

YELLOW = '#f7f5dd'
PANTEON = '#C9B27C'
PINK = '#e2979c'
GREEN = '#9bdeac'
COS = '#F0F7D4'
FONT = ('Courier',12,'bold')
passwd = ''

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
  global passwd
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_list = []
  password_list.extend(choice(letters) for _ in range(randint(8,10))) # generator
  password_list += [choice(symbols) for _ in range(randint(2,4))] # adding list created in memory
  password_list.extend([choice(numbers) for _ in range(randint(2,4))]) # list extended by a second list
  shuffle(password_list)
  password = ''.join(password_list)

  passw_entry.delete(0,tk.END)
  passw_entry.insert(0, password)
  passwd = password[:]
  return password

def copy_to_clip():
  pyperclip.copy(passwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
  # end_string = ts.string_concat(web_entry.get(), email_user_entry.get(), passw_entry.get())
  website = web_entry.get()
  new_data = {
    website: { # website - czyli ten niby klucz, musi byc zainicjowana zmienna, musi miec wartosc, czyli to nie taki "klucz"
      "email":email_user_entry.get(),
      "password":passw_entry.get()
    }
  }
  is_ok = tkinter.messagebox.askokcancel(title='Question',message=f'url: {web_entry.get()}\npass: {passw_entry.get()}\nlogin: {email_user_entry.get()}\n Are above date correct ?')
  if (web_entry.get() == '' or email_user_entry.get() == '' or passw_entry.get() == ''):
    tkinter.messagebox.showerror(title='Ooops !',message ='Please don\'t leave any fields empty!',icon='warning')
  elif is_ok:
    try:
      with open('data.json','r') as data_file:
        # data_file.write(end_string)
        data = json.load(data_file) # odczyt z pliku
        data.update(new_data) # updejt pliku o to co wprwoadziles button_add
        # zapis do pliku na dysku, wymaga zeby zamknac plik i znowu otworzyc inaczej WRON ! xD
    except FileNotFoundError:
      print('File not found !')
      with open('data.json','w') as data_file:
        json.dump(new_data,data_file, indent = 4) # json.dump to inaczej file.write(), 1 arg to co dumpisz 2 arg do czego dumpisz
      print('File was created')
    except json.decoder.JSONDecodeError:
      print('File exists but it\'s empty')
      with open('data.json','w') as data_file:
        json.dump(new_data,data_file, indent = 4) # json.dump to inaczej file.write(), 1 arg to co dumpisz 2 arg do czego dumpisz
    else:
      with open('data.json','w') as data_file:
        json.dump(data,data_file, indent = 4) # json.dump to inaczej file.write(), 1 arg to co dumpisz 2 arg do czego dumpisz
    finally: # bez tego też zadziala, tzn wykona sie po try/exce pt ale z finally wyglada more pro
      web_entry.delete(0,tk.END)
      email_user_entry.delete(0,tk.END)
      passw_entry.delete(0,'end')
      return print('Zapisano dane do pliku results.txt')

# ---------------------------- SEARCHING FUNCTIONALITY -----------------#
def find_password():
  try:
    with open('data.json','r') as json_file:
      data = json.load(json_file)
  except FileNotFoundError:
    pass
    print('File with data doesn\'t exist')
    tk.messagebox.showinfo(title = 'Info',message = 'File with data not found!', icon = 'warning')
    file = open('data.json','w')
    file.close()
    print('File was created')
  except json.decoder.JSONDecodeError:
    print('Searched website haven\'t been found, maybe file  is empty ?')
    tk.messagebox.showinfo(title = 'Info', message = 'Searched phrase not found', icon = 'info')
  else:
      # print(data.keys())
      key_inputed = web_entry.get()
      key_list = [key for key in data.keys()]
      if key_inputed in key_list:
        email_user_entry.delete(first = 0, last = tk.END)
        passw_entry.delete(first = 0, last = tk.END)
        email_user_entry.insert(index = 0, string = data[key_inputed]['email'])
        passw_entry.insert(index = 0, string = data[key_inputed]['password'] )
        tk.messagebox.showinfo(title='Information', message = f'login: {data[key_inputed]['email']}\npassword: {data[key_inputed]['password']}', icon = 'info', default = 'ok')
      else:
        print('Searched phrase not found')
        tk.messagebox.showinfo(title = 'Key not found', message = 'Searched phrase not found', icon = 'info')


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
generate_button = tk.Button(text='Generate Password:', bg = COS, command = password_generator, width = 20)
generate_button.grid(column = 2, row = 6)
copy_button = tk.Button(text='Copy Password', bg = COS, command = copy_to_clip, width = 20)
copy_button.grid(column = 2, row = 7)
search_button = tk.Button(text = 'Search', bg = COS, width = 20, command = find_password)
search_button.grid(column = 2, row = 4)

#Entrypoints
web_entry = tk.Entry(width = 42)
web_entry.grid(column = 1, row = 4, columnspan = 2, sticky ='w')
web_entry.focus()
web_entry.insert(tk.END,'www.ins...') # END to stała z biblioteki tkinter, 0 początek, end koniec

email_user_entry = tk.Entry(width = 42)
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
# canvas.create_text(100,100,text='lubie cycki', font=("Ariel",40,"italic"))

window.mainloop()
