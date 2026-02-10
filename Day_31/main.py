import tkinter as tk
import csv
from tkinter import Canvas, PhotoImage
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data= pandas.read_csv("data/french_words.csv")

word = {}
dict_of_words =[]


# func
def next_card():
  global word, flip_timer,dict_of_words
  window.after_cancel(flip_timer)
  list_of_words = [(index,key) for (index,key) in data.items()]
  dict_of_words = data.to_dict(orient='records') # magic options, make list of dicts
  print(dict_of_words)
  # random.randint(1,len(dict_of_words))
  word = random.choice(dict_of_words)
  print(type(word))
  print(word)
  canvas.itemconfig(card_side,image=card_front)
  canvas.itemconfig(card_title,text='French', fill='black')
  canvas.itemconfig(card_word,text=word['French'], fill='black')
  window.after(ms=3000, func=change_side)

def change_side():
  global word, flip_timer
  canvas.itemconfig(card_side,image=card_back)
  canvas.itemconfig(card_title,text='English', fill='white')
  canvas.itemconfig(card_word,text=word['English'], fill='white')

def remove_card():
  global word,dict_of_words
  print(f'{word}removed')
  dict_of_words.remove(word)
  data = pandas.DataFrame(dict_of_words)
  data.to_csv('data/words_to_learn.csv')
  next_card()



# window
window = tk.Tk()
window.title(string='Flashy')
window.configure(height=800, width=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(ms=3000, func=change_side)

canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
card_side = canvas.create_image(400,263,image=card_front)
card_title = canvas.create_text(400,150,text='Title',font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text='Word',font=("Times News Roman",60,"bold"))

canvas.grid(column=0,row=0, columnspan=3)

#buttons
my_image = PhotoImage(file='./images/wrong.png')
wrong_button = tk.Button(image=my_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=2,row=2)
my_image1 = PhotoImage(file='./images/right.png')
right_button = tk.Button(image=my_image1, highlightthickness=0, command=remove_card)
right_button.grid(column=0,row=2)

next_card()

window.mainloop()