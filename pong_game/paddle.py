from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__() # this function inherits from Turtle class and initiates attributes (default values)
    self.shape('square')
    self.shapesize(stretch_wid=5,stretch_len = 1)
    self.color('white')
    self.penup()
    self.goto(position)

  def go_down(self):
    new_y_pos = self.ycor() - 20
    self.goto(self.xcor(),new_y_pos)

  def go_up(self):
    new_y_pos = self.ycor() + 20
    self.goto(self.xcor(),new_y_pos)



