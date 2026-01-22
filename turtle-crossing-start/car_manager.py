from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """ generator samochodzików :)"""
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len = 2, stretch_wid = 1)
        self.goto(250,random.randint(-250,250))
        self.setheading(180)
        self.move_car()
        self.speed = STARTING_MOVE_DISTANCE

    def move_car(self, speed = STARTING_MOVE_DISTANCE):
        self.forward(speed)

    def move_faster(self):
        return self.speed