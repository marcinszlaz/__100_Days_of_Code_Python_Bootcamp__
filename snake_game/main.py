from turtle import Turtle, Screen
from snake import Snake
import random
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snakers = Snake()
screen.listen() # ekran słucha, co klikniesz
screen.onkey(snakers.up,'Up')  # tutaj tworzysz definicję, na jakie klawisze co ma robić ekran
screen.onkey(snakers.down,'Down')
screen.onkey(snakers.right,'Right')
screen.onkey(snakers.left,'Left')
fuut = Food()
scoreboard = Score()

# snakers.create_snake() # to jest nadmiarowe, wydłuża węża xD bo sam Snake() odopala create_snake() bo ta funkcja
# jest w konstruktorze __init__

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.3)
  snakers.move()

  # collision detection with food
  if snakers.head.distance(fuut) < 15:
    scoreboard.druknij()
    fuut.refresh()
    snakers.extend()
  # collision detection with walls
  if snakers.head.xcor() < -300 or snakers.head.xcor() > 300 or snakers.head.ycor() < -300\
          or snakers.head.ycor() > 300:
    game_is_on = False
    scoreboard.game_over()
  # detection collision with tail.

  for segment in snakers.segments[1:]: # dzieki slicing pomijasz 0 indeks, czyli głowę wensza xD
    if snakers.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()

  # for segment in snakers.segments:
  #   if segment == snakers.head:
  #     pass
  #   elif snakers.head.distance(segment) < 10:
  #     game_is_on = False
  #     scoreboard.game_over()

screen.exitonclick()