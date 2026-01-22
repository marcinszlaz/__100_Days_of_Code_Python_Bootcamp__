from turtle import Turtle, Screen
from random import randint

winner = ''
tim = Turtle()
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title='Make you bet', prompt='Which turtle will win the race? Enter a color: ')
turtle_colors = ['red','orange','yellow','green','blue','purple']
turtle_list = []
turtle_dict = {}

print(screen.getshapes())


for color in turtle_colors:
  turtle_dict[color+'_turtle'] = Turtle()


while user_bet not in [turtle for turtle in turtle_dict]:
  print(f'Wrong turtle inputed ! { ', '.join(turtle_dict.keys())}')
  # tak też dziala xD, to moje :) { ', '.join([f'{turtle}' for turtle in turtle_dict])} ', ' join sam pilnuje
  # zeby znak separacji sam byl po wyniku i nie wstawia znaku `,` na koncu :)
  user_bet = screen.textinput(title='Make you bet', prompt='Which turtle will win the race? Enter a color: ')
else:
  i = 0
  x = 0
  for turtles in turtle_dict:
    turtle_dict[turtles].shape('turtle')
    turtle_dict[turtles].up()
    turtle_dict[turtles].color(turtle_colors[i])
    i += 1
    turtle_dict[turtles].goto(-240,150 - x)
    x += 50

  print(turtle_dict)

  finish_line = False
  while not finish_line:
    for turtles in turtle_dict:
      random_jump = randint(1, 10)
      turtle_dict[turtles].forward(random_jump)
      if turtle_dict[turtles].xcor() >= 225:
        finish_line = True
        winner = turtles
        print(f'{winner} is the winner !')
        if winner == user_bet:
          print('You\'r turtle win the race !')
        else:
          print('You loose and nobody loves you !')
        break

  screen.exitonclick()

