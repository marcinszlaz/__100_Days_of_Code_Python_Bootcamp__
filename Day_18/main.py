import turtle
from turtle import Turtle, Screen
from figures import Figures

timmy = Turtle()
action = Figures(timmy)
turtle.colormode(255)

timmy.shape('classic') # arrow, square, circle, turtle, triangle
timmy.shapesize(1, 1, 1)
timmy.color('chartreuse')
timmy.pencolor('red')
timmy.up()
timmy.setposition(0,0)
timmy.down()
timmy.speed(0)
# timmy.setheading()
timmy.pensize(1)
# action.triangle()
# action.square()
# action.pentagon()
# action.hexagon()
# action.octagon()
# for sides_number in range(3,10):
#   action.how_many(sides_number)

# licznik = 1
# while licznik < 2000: # mozna użyc funkcji setheading() xD
#   action.how_many_rand()
#   licznik += 1

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)
for i in range(36):
  timmy.pencolor(action.rand_color_tuple_generator())
  timmy.circle(100)
  cur_heading = timmy.heading()
  timmy.setheading(cur_heading + 10)

screen = Screen()
screen.setup(width=800, height=600)
screen.exitonclick() # musisz to miec zeby ekranik troche powisial :)

