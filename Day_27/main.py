import tkinter
import random

# from tkinter import *

# window creation
window = tkinter.Tk()
window.title("My First GUI program :-)")
window.minsize(width = 500, height=300)

# label creation
my_label = tkinter.Label(text="I Am a Liquor !", font = ("Arial",12,"bold")) # tworzy label
my_label.pack(side = "top") # wrzuca label na ekran :) expand=True, "left", "right"

my_label["text"] = 'Zupa' # mozna tak zmienic tekst
# i tak też, funkcja config
# mozna tak dodawac bo biblioteka jest przepisana z tcl innego jezyka
# i argumenty w tej clasie sa prawie wszedzie jako *args czyli tuple () z wieloma arg np 1,2,3
# albo *kwargs czyli keyword arguments i to są z kolei słowniki {} czyli 'x':5,'y':'zupa' itp
my_label.config(text = 'Jak to jest')

slownik = ['Clicking and clicking','Stop clicking me !','maybe you will stop clicking xD', 'And he\'s again doing the same']
def click_me():
  # my_label.config(text = f'{random.choice(slownik)}') # opcja randomowych odpowiedzi
  my_label.config(text = input.get())

button = tkinter.Button(text='Click me', command = click_me)
button.pack() # musisz dodawać pack zeby sie pokazalo xD

input = tkinter.Entry(width =10)
print(input.get()) # to nic tu nie wydrukuje musisz to zrobic funkcja
my_label.config(text = input.get())
input.pack()

# import turtle
# tim = turtle.Turtle()
# tim.write("cycki")


window.mainloop() # same like in turtle
