import turtle

import colorgram
import kropki
from turtle import Turtle, Screen
from random import choice

turtle.colormode(255)
color_table = kropki.color_list()
timmy = Turtle()
action = Screen()

# turtle settings
timmy.shape('arrow')
timmy.pensize(3)
timmy.pencolor('red')
timmy.up()
timmy.hideturtle()
timmy.setposition(-360,-295) # mozna też użyć timmy.setheading(azymut xD) tak, heading w navigacji to azymut xD
timmy.speed('fastest')

# print(choice(color_table))
# print(type(choice(color_table)))
# print(timmy.pencolor(choice(color_table)))

# iterator = 10
# y = 40
# while iterator != 0:
#   iterator -= 1
#   for _ in range(10):
#     timmy.dot(30,choice(color_table))
#     timmy.forward(50)
#   timmy.setposition(-380,-300 + y)
#   y += 40
y = 40
for _ in range(16):
  for _ in range(15):
    timmy.dot(30,choice(color_table))
    timmy.forward(50)
  timmy.setposition(-355,-295 + y)
  y += 40


# screen settings
action.exitonclick()
# action.title('Zolwik')

