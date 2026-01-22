import random
from color_dict import colors, right_direction

class Figures:
  """class constructor expects turtle class object as parameter"""
  def __init__(self, turtle):
    self.timmy = turtle
    self.full_angle = 360
    self.triangle_sides = 3
    self.square_sides = 4
    self.pentagon_sides = 5
    self.hexagon_sides = 6
    self.octagon_sides = 8
    self.sides = 0

  def how_many(self, sides):
    """ how many sides our figure may have ?"""
    self.sides = sides
    for _ in range(self.sides):
      self.turtle_move()
      self.turn()

  def how_many_rand(self):
    """ how many sides our figure may have ?"""
    self.turn_rand()
    self.turtle_move_rand_angle()

  def triangle(self):
    """ method draws triangle"""
    self.sides = self.triangle_sides
    for _ in range(self.sides):
      self.turtle_move()
      self.turn()

  def square(self):
    """method draws square"""
    self.sides = self.square_sides
    for _ in range(self.sides):
      self.turtle_move()
      self.turn()

  def pentagon(self):
    """method draws pentagon"""
    self.sides = self.pentagon_sides
    for _ in range(self.sides):
      self.turtle_move()
      self.turn()

  def hexagon(self):
    """method draws hexagon"""
    self.sides = self.hexagon_sides
    for _ in range(self.sides):
      self.turtle_move()
      self.turn()

  def octagon(self):
    """method draws octagon"""
    self.sides = self.octagon_sides
    for _ in range(self.sides):
      self.turtle_move()
      self.turn()

  def turn(self):
    """method make turns, angle depends on figure drawn with"""
    self.timmy.left(self.full_angle/self.sides)

  def turn_rand(self):
    """method turn_rand make turns, angle depends on random.choice() => (90,180,270,360 degrees)"""
    self.timmy.left(random.choice(right_direction))

  def rand_color_tuple_generator(self):
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    # random_color = (red,green,blue)
    # return random_color
    return red,green,blue

  def turtle_move(self):
    # self.timmy.pencolor(random.choice(colors))
    self.timmy.pencolor(self.rand_color_tuple_generator())
    for i in range(10):
      # self.timmy.pencolor(random.choice(['red','blue','green']))
      self.timmy.forward(7)
      self.timmy.up()
      self.timmy.forward(3)
      self.timmy.down()

  def turtle_move_rand_angle(self):
    # self.timmy.pencolor(random.choice(colors))
    self.timmy.pencolor(self.rand_color_tuple_generator())
    for i in range(1):
      rand_step_lenght = random.randint(5,10)
      self.timmy.forward(rand_step_lenght)
      self.timmy.up()
      self.timmy.forward(rand_step_lenght)
      self.timmy.down()

  # for _ in range(len(colors)):
  #   # self.timmy.pencolor(colors[_])
  #   print(_)
  #   print(colors[_])


