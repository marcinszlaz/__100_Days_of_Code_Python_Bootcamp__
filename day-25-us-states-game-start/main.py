import turtle
import pandas as df
import prettytable
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
# screen.bgpic("./blank_states_img.gif")
image = 'blank_states_img.gif'
screen.addshape(image) # this function add new shape to the turtle shapes list, after that we need choose turtle shape
turtle.shape(image)

# fun onscrenclick gets fun as argument, fun must have two args too
def where_am_i_click(x,y):
  print(x,y)

turtle.onscreenclick(where_am_i_click)

# with csv.reader()
# score = 0
# correct_answers = []
# while len(correct_answers) < 50:
#   answer_state = (turtle.textinput(f"{score}/50 States Correct", 'What\'s another state\'s name?')).title()
#   if answer_state == 'Exit':
#     break
#   with open('50_states.csv', mode = 'r') as file:
#     file_content = csv.reader(file)
#     for row in file_content:
#       if row[0] == answer_state:
#         new_turtle = turtle.Turtle()
#         new_turtle.hideturtle()
#         new_turtle.penup()
#         x = int(row[1])
#         y = int(row[2])
#         new_turtle.goto(x,y)
#         new_turtle.write(f'{answer_state}')
#         score += 1
#         correct_answers.append(answer_state)
#
# all_answers = []
# with open('50_states.csv', mode = 'r') as file:
#   stat_content = csv.reader(file)
#   tmp_list = []
#   for row in stat_content:
#     tmp_list.append(row[0])
#     all_answers = tmp_list
#
# what_lasts = set(all_answers) - set(correct_answers)
# print(len(what_lasts)-1)
# with open('states_to_learn.csv',mode = 'w') as file:
#   file.write(str(what_lasts))

# with pandas
score = 0
correct_answers = []
while True:
  answer_state = (turtle.textinput(f'{score}/50 States Correct', 'What\'s another state\'s name?')).title()
  if answer_state == 'Exit':
    break
  states_list = df.read_csv('50_states.csv') # utworzenie listy stanów pandasem xD
  # if df['state'].isin([answer_state]).any(): # wbudowane metody isin czy jest w? any() zeby sprawdzic kazdy row
  if answer_state in states_list.state.to_list():
    row_xy = states_list[states_list['state'] == f"{answer_state}" ]
    xp = row_xy.x.to_list()[0] # instead of this row_xy.x.item() => elegant way, but my way works to xD
    yp = row_xy.y.item()
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(xp, yp)
    new_turtle.write(f'{answer_state}')
    score += 1
    correct_answers.append(answer_state)

a_s = df.read_csv('50_states.csv')
a_s_list = a_s['state'].to_list()
to_learn = set(a_s_list).difference(set(correct_answers))
df.DataFrame(to_learn).to_csv('states_to_learn.csv')

#screen.mainloop() # it fits more, cos we have loop but program doesn't exit on click
# screen.exitonclick() # exit on click, that's no good for this program
