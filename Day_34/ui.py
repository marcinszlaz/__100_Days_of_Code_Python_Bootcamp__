import tkinter as t
from quiz_brain import QuizBrain as Q

THEME_COLOR = "#375362"
CV_BG_COLOR = "#E4E4E4"


class QuizInterface:

  def __init__(self):
    # window
    self.window = t.Tk()
    self.window.title("Quizzler")
    self.window.configure(width=600, height=550, padx=30,pady=30)
    self.window.config(bg=THEME_COLOR,padx=40, pady=40)
    # label
    self.score_label = t.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
    self.score_label.grid(row=0,column=1)
    # canvas
    self.canvas = t.Canvas(bd=5,bg=CV_BG_COLOR, highlightthickness=0, height=250, width=300, )
    self.canvas.grid(column=0, row=1,columnspan=3)
    self.q_text = self.canvas.create_text(150,125,text='Some text', justify='center',angle=-2, font=("Calibri",20,"italic"))
    self.canvas.itemconfig(self.q_text, text='DUPA')
    # buttons
    self.no_image = t.PhotoImage(file='./images/false.png')
    self.yes_image = t.PhotoImage(file='./images/true.png')
    self.yes_button = t.Button(command=Q.next_question,image=self.yes_image,highlightthickness=0)
    self.yes_button.grid(column=0, row=4, pady=(20,20)) # góra, dół
    self.no_button = t.Button(command='',image=self.no_image,highlightthickness=0)
    self.no_button.grid(column=2,row=4, pady=20)

    self.window.mainloop()


