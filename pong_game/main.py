from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
import random
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title('Ping Pong')
screen.tracer(0)

l_paddle = Paddle((-385,0)) # constructor class demand tuple as parameter
r_paddle = Paddle((385,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(l_paddle.go_down,'s')
screen.onkey(l_paddle.go_up,'w')

game_is_on = True
while game_is_on:
  ball.ball_move()
  sleep(0.1)
  # print(ball.distance(l_paddle))
  # print(ball.distance(r_paddle))
  print(r_paddle.distance(ball))
  if abs(ball.distance(r_paddle)) < 30 and ball.xcor() > 350:
    ball.bounce_ball()
    ball.ball_move()
  elif abs(ball.distance(l_paddle)) < 30 and ball.xcor() > -350:
    ball.bounce_ball()
    ball.ball_move()

  screen.update()

screen.exitonclick()
