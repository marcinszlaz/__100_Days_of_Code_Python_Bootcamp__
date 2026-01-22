import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

speed = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title('Hit the road Jack ! xD')

player = Player()
cars = CarManager()
cars_fleet = []
cars_fleet.append(cars)
score = Scoreboard()

screen.onkey(fun = player.move_up, key ="Up")

game_is_on = True
loop_counter = 0
while game_is_on:
    for _ in range(0,len(cars_fleet)):
        cars_fleet[_].move_car(speed)
        if player.distance(cars_fleet[_]) < 15:
            print('Game Over Mr Turtle!')
            game_is_on = False
            score.game_over()
            screen.update()
            time.sleep(3)

    time.sleep(0.1)
    loop_counter += 1
    if loop_counter % 6 == 0:
        cars = CarManager()
        cars_fleet.append(cars)
    if player.ycor() > 280:
        player.ha_teleport()
        speed += 10
        score.score += 1
        score.clear()
        score.level(score.score)

    screen.update()
