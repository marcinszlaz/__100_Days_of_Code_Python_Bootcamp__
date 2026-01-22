from turtle import Turtle
import random

ANGLE_LIST = [30, 45, 50, 330, 315, 310,150,120,135,225,130,230]

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape('circle')
    self.shapesize(stretch_wid = 1, stretch_len = 1)
    self.color('green')
    self.goto(0,0)
    self.rand_angle_ = 0
    self.rpaddle_point = 0
    self.lpaddle_point = 0

  def rand_angle(self):
    angle =  random.randint(0,359)
    while (45 < angle < 135) or (225 < angle < 315):
      angle = random.randint(0,359)
    else:
      self.rand_angle_ =  angle

  def bounce_ball(self):
    direction = self.heading()
    self.setheading(direction + random.choice([180,270,90]))
    self.forward(5)

  def ball_move(self):
    if self.position() == (0,0):
      self.setheading(random.choice(ANGLE_LIST))
      self.rand_angle_ = self.heading()
      self.forward(5)
    elif abs(self.ycor()) > 280:
      #self.ycor() in [300,-300]: albo self.ycor() >300 or self.ycor() < 300 z abs jest bardziej elegancko (wartosc bezwzgledna), poza tym musi byc wieksze niż bo jakby przeskoczylo z 299 na 304 powiedzmy (przy roznych katach taki
      # scenariusz jest mozliwy) to wtedy 'nie ma sciany'
      dir = self.heading()
      if 90 < dir < 180:
        self.setheading(dir + 45)
      elif 180 < dir < 270:
        self.setheading(dir - 45)
      else:
        self.setheading(0-self.rand_angle_)
        self.forward(3)
    elif abs(self.xcor()) > 380:
      if self.xcor() > 380:
        self.lpaddle_point += 1
        self.reset_position()
      else:
        self.rpaddle_point += 1
        self.reset_position()
    else:
      self.forward(5)

  def reset_position(self):
    self.goto(0,0)

# test=Ball()
# angle = test.rand_angle()
# print(test)
# print(angle)
