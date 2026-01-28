# from tkinter import * # with this astrix import You are able to type methods/functions directly
# without tkinter. prefix

import tkinter
FONT = ("Arial",12,"bold")
CONV_RATE = 1.609

# window creation
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width = 300, height=150)
window.config(padx = 10, pady = 10)
window.config(padx = 20, pady = 20) # pad setting

# entry
input_content = tkinter.Entry(width = 10)
input_content.grid(column = 2, row = 2)

# functions block
def cvrt_m_to_k():
  """function cvrt_m_to_k converts mile to kilometers"""
  label2.config(text = f'{(float(input_content.get()) * CONV_RATE):.2f}')

# label creation
label1 = tkinter.Label(text="Is equal to", font = FONT) # is equal label
label1.grid(column=1,row = 3)

label2 = tkinter.Label(text = '0', font = FONT) # label with result
label2.grid(column = 2, row = 3)

label3 = tkinter.Label(text="Miles", font = FONT) # Miles label
label3.grid(column = 3, row = 2)

label4 = tkinter.Label(text = "Km", font = FONT) # Km label
label4.grid(column = 3, row = 3)

# button
button1 = tkinter.Button(text = 'Calculate',command = cvrt_m_to_k)
button1.grid(column = 2, row = 4)

window.mainloop() # same like in turtle, looping the window
