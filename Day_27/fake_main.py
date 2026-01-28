import tkinter
import random

# from tkinter import *

# window creation
window = tkinter.Tk()
window.title("My First GUI program :-)")
window.minsize(width = 500, height=300)
window.config(padx = 10, pady = 10)

# label creation
my_label = tkinter.Label(text="I Am a Liquor !", font = ("Arial",12,"bold")) # tworzy label
my_label.grid(column=1,row = 1) # wrzuca label na ekran :) expand=True, "left", "right" to sie tyczy place()

my_label["text"] = 'Zupa' # mozna tak zmienic tekst
# i tak też, funkcja config
# mozna tak dodawac bo biblioteka jest przepisana z tcl innego jezyka
# i argumenty w tej clasie sa prawie wszedzie jako *args czyli tuple () z wieloma arg np 1,2,3
# albo *kwargs czyli keyword arguments i to są z kolei słowniki {} czyli 'x':5,'y':'zupa' itp
my_label.config(text = 'Jak to jest')

slownik = ['Clicking and clicking','Stop clicking me !','maybe you will stop clicking xD', 'And he\'s again doing the same']
def click_me():
  # my_label.config(text = f'{random.choice(slownik)}') # opcja randomowych odpowiedzi
  pole_wejsciowe = input.get()
  if not pole_wejsciowe:
    my_label.config(text = 'Jak żyć, jak żyć')
    my_label.grid(column = 1, row = 1)
  else:
    my_label.config(text = input.get())

my_label.config(text = 'zupa')
my_label.grid(column = 1, row = 1)
button = tkinter.Button(text='Click me', command = click_me)
button.grid(column = 2, row = 2) # musisz dodawać pack zeby sie pokazalo xD

new_button = tkinter.Button(text = 'New button')
new_button.grid(column = 3, row = 1)

# entry
input = tkinter.Entry(width =10)
print(input.get()) # to nic tu nie wydrukuje musisz to zrobic funkcja
my_label.config(text = input.get())
input.grid(column = 3, row = 3) # to jest tzw layout manager inne menadzery to place(x,y) i grid() without them created objects don't show up
# one word of warning ! You cannot mix it up ! nie mozesz miec jednoczesnie pack() i grid() bo sie PSUJE xD

# import turtle
# tim = turtle.Turtle()
# tim.write("cycki")

window.mainloop() # same like in turtle
