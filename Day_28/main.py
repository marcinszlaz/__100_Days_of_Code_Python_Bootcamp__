import tkinter as tk
from tkinter import Canvas, PhotoImage
import math

# start 09:50
# przerwa 12:20
# powrót 13:00
# end P28 14:00
# mysql 15:00
# mysql end 16:30
# mysql 19-21:30 7:30h, 5h mysql/ 2:30 python
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SEC_MIN = 60
reps = 0
timer = None
text = 'Timer'
timer_label = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
  global timer
  global reps
  window.after_cancel(timer)
  canvas.itemconfig(timer_text,text='00:00')
  timer_label.config(text=text)
  check_mark.config(text='')
  reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
  global reps
  global text
  global timer_label
  reps += 1
  print(reps)
  work_sec = SEC_MIN * WORK_MIN
  short_break_sec = SEC_MIN * SHORT_BREAK_MIN
  long_break_sec = SEC_MIN * LONG_BREAK_MIN
  # while - nie da sie :) mrozi program trzeba uzywac windows.after / after_cancel
  if reps in [1,3,5,7]:
    count_down(work_sec)
    timer_label.config(text = 'WORK', fg = GREEN, bg = YELLOW)
  elif reps in [2,4,6]:
    count_down(short_break_sec)
    timer_label.config(text = 'Break', fg = PINK, bg = YELLOW)
  else:
    count_down(long_break_sec)
    timer_label.config(text = 'BREAK', fg = RED, bg = YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
  global timer
  global reps
  if count > 0:
    canvas.itemconfig(timer_text, text = f'{count // 60}:{count % 60:02d}')
    timer = window.after(1000, count_down, count -1)
  elif count == 0:
    start_timer()
    sign = '✓' * (reps//2)
    check_mark.config(text=sign)

# def count_down(count):
#   count_min = math.floor(count / 60) #count // 60
#   count_sec = count % 60
#   if count_sec == 0:
#     count_sec = '00' # tu jest też problem z 9,8,7 bo robi jeden digit bez 0
#   elif 0 < count_sec < 10:
#     count_sec = f'0{count_sec}' # MIND FUCK MODE ON xD to nie concat str z int tylko samo str 09, 08
#   if count > 0:
#     canvas.itemconfig(timer_text, text = f' {count_min}:{count_sec} ')
#     window.after(1000, count_down, count -1)
# można też użyć import math math.floor(count/60)
# zamiast text = f'{count // 60}:{count % 60:02d} ', bo to przesuwa tekst w lewo można użyć
# if time_in_sec == 0 time_in_sec = '00' w funkcji start_timer lub na odwrót, to z if to byl moj
# pierwszy pomysł, przesuniecie w lewo występuje w każdej opcji i z if i z floor
# okazało sie ze sposobem na to jest spacja w argumencie text f' {, to rozwiązało problem
# a tak naprawdę problemem był } ' ta spacja na końcu xDDD
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodore")
window.config(padx=100, pady = 50, bg=YELLOW)

timer_label = tk.Label(text = text,font = (FONT_NAME,50,"bold"), fg = GREEN, bg = YELLOW)
timer_label.grid(column = 1, row = 0)

start_button = tk.Button(text = 'Start', command = start_timer)
start_button.grid(column = 0,row = 2)

reset_button = tk.Button(text = 'Reset', command = reset_timer)
reset_button.grid(column = 2, row = 2)

check_mark = tk.Label(fg = GREEN, bg = YELLOW)
check_mark.grid(column = 1, row = 3)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,118, text = '00:00', fill='white',font=(FONT_NAME,35,'bold'))
# canvas.create_text(100,0, text = 'Timer', fill=GREEN,font=(FONT_NAME,35,'bold')) # to jednak nie może być z canvas
# bo jest przycięte przed płótno

canvas.grid(column = 1, row = 1)
window.mainloop()

# kod pomocniczy
# def say_something(thing):
#   print(thing)
#
# window.after(1000, func = say_something, 'Hello') # ta funkcja, jako 3 argument args* przyjmuje coś co wstrzyknie,
#swojego drugiego argumentu func (funkcja), czyli wstrzykuje 3 argument jako argument dla funkcji w func =
