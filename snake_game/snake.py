from turtle import Turtle, Screen
import random
import time

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)] # variable constans w pyton pisze sie DUŻYMI LITERAMI (tzn ich nazwe)
MOVE_DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  def add_segment(self,position):
      new_segment = Turtle('square')
      new_segment.up()
      new_segment.color('white')
      new_segment.goto(position)
      self.segments.append(new_segment)

  def extend(self):
    self.add_segment(self.segments[-1].position())

  def move(self):
    for seg in range(len(self.segments) - 1, 0, -1): # lenght 3, 3-1 = 2, liczy 2,1 nie liczy 0 bo range nie liczy stop
      # kleje jak to działa ale nie wpadłbym na takie rozwiązanie, że ostatni wchodzi
      # na pozycje przed nim, przedostatni na pozycje tego przed nim i tak każdy nachodzi na siebie, w ten sposób
      # cialo zawsze będzie podążać za głowa węża
      xpos = self.segments[seg - 1].xcor()
      ypos = self.segments[seg - 1].ycor()
      self.segments[seg].goto(xpos, ypos)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)




