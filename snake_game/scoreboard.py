from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier',12,'bold')

class Score(Turtle):
  def __init__(self):
   super().__init__()
   self.score = 0
   self.goto(-10,275)
   self.penup()
   self.color('white')
   self.hideturtle()
   self.druknij()

  def druknij(self):
   self.clear()
   self.write(f"Score: {self.score}", move = False, align =ALIGNMENT, font = FONT)
   self.score += 1

  def game_over(self):
   self.goto(0,0)
   self.write("GAME OVER", move = False, align =ALIGNMENT, font = FONT)

