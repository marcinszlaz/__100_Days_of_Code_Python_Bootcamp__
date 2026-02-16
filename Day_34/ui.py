import html
import tkinter as t
from quiz_brain import QuizBrain # dzięki temu importowi

THEME_COLOR = "#375362"
CV_BG_COLOR = "#E4E4E4"


class QuizInterface:

  def __init__(self,quiz: QuizBrain): # i temu określeniu typu przyjmowanego parametru
    #QuizBrain class object
    self.quiz = quiz
    # window
    self.window = t.Tk()
    self.window.title("Quizzler")
    self.window.configure(width=600, height=550, padx=30,pady=30)
    self.window.config(bg=THEME_COLOR,padx=40, pady=40)
    # label
    self.score_label = t.Label(text=f'Score: {self.quiz.score}', fg="white", bg=THEME_COLOR, font=('Arial',15,'italic'))
    self.score_label.grid(row=0,column=2, sticky='E')
    # canvas
    self.canvas = t.Canvas(bd=5,bg=CV_BG_COLOR, highlightthickness=0, height=250, width=300)
    self.canvas.grid(column=0, row=1,columnspan=3)
    self.q_text = self.canvas.create_text(150,125,text='Welcome in Quizzler!', justify='center',angle=-2, font=("Calibri",20,"italic"), width=300)
    # buttons
    self.no_image = t.PhotoImage(file='./images/false.png')
    self.yes_image = t.PhotoImage(file='./images/true.png')
    self.yes_button = t.Button(command=self.answer_yes,image=self.yes_image,highlightthickness=0)
    self.yes_button.grid(column=0, row=4, pady=(20,20)) # góra, dół
    self.no_button = t.Button(command=self.answer_no,image=self.no_image,highlightthickness=0)
    self.no_button.grid(column=2,row=4, pady=20)
    # function called
    self.get_next_question()

    self.window.mainloop()

  def get_next_question(self):
    if self.quiz.still_has_questions():
      text = self.quiz.next_question()
      self.canvas.itemconfig(self.q_text, text=text)
    else:
      self.canvas.itemconfig(self.q_text, text=f'You\'ve completed the quiz. Your final score was: {self.quiz.score}/{self.quiz.question_number}')
      self.yes_button.config(state='disabled')
      self.no_button.config(state='disabled')


  def answer_yes(self):
    user_input = 'True'
    self.give_feedback(self.quiz.check_answer(user_input))
    self.score_label.config(text=f'Score: {self.quiz.score}')

  def answer_no(self):
    user_input = 'False'
    self.give_feedback(self.quiz.check_answer(user_input))
    self.score_label.config(text=f'Score: {self.quiz.score}')

  def give_feedback(self,is_right: bool):
    if is_right:
      self.green_flash()
      self.window.after(1000,func=self.get_next_question)
    else:
      self.red_flash()
      self.window.after(1000,func=self.get_next_question)

  def green_flash(self):
    self.canvas.config(bg='green')
    self.window.after(1000,func=self.bg_return)

  def red_flash(self):
    self.canvas.config(bg='red')
    self.window.after(1000,func=self.bg_return)

  def bg_return(self):
    self.canvas.config(bg=CV_BG_COLOR)
