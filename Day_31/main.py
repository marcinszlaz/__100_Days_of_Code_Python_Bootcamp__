import tkinter as tk
import csv
from tkinter import Canvas, PhotoImage
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data= pandas.read_csv("data/french_words.csv")

# func
def next_card():
  list_of_words = [(index,key) for (index,key) in data.items()]
  dict_of_words = data.to_dict(orient='records') # magic options, make list of dicts
  # random.randint(1,len(dict_of_words))
  word = random.choice(dict_of_words)
  canvas.itemconfig(card_title,text='French')
  canvas.itemconfig(card_word,text=word['French'])

window = tk.Tk()
window.title(string='Flashy')
window.configure(height=800, width=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas = Canvas(width=200,height=224, bg=PANTEON, highlightthickness=0)
# tomato_img = PhotoImage(file='logo.png')
# canvas.create_image(100,112,image=tomato_img)
# canvas.grid(column = 1, row = 0)

canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
canvas.create_image(400,263,image=card_back)
card_title = canvas.create_text(400,150,text='Title',font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text='Word',font=("Times News Roman",60,"bold"))

canvas.grid(column=0,row=0, columnspan=3)

#buttons
my_image = PhotoImage(file='./images/wrong.png')
wrong_button = tk.Button(image=my_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=2,row=2)
my_image1 = PhotoImage(file='./images/right.png')
right_button = tk.Button(image=my_image1, highlightthickness=0, command=next_card)
right_button.grid(column=0,row=2)


window.mainloop()