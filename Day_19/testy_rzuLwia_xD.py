from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.setheading(90)

def napszut_xD():
  tim.forward(10)

def f_tyu_xD():
  tim.backward(10)

def lewo():
  tim.left(10)

def prawo():
  tim.right(10)

def wyczysc():
  tim.clear()

def pozycja_wyjsciowa():
  tim.up()
  tim.setposition(0,0)
  tim.down()

screen.listen()
screen.onkey(fun = napszut_xD, key = 'w' ) # napszut_xD mowi onkey, tu jest adres funkcji, jak ktos kliknie Up to ją
# uruchom, napszut_xD() -> tu jest funkcja, odpal ją, bo () to operator wywołania, z adresem ale bez wywołania onkey
# sam sobie odpala funkcję a trigerem jest Up, wciskasz Up, onkey dodaje () do adresu obiektu i wykonuje funkcje, sklejasz
# baze ? xD
screen.onkey(fun = f_tyu_xD, key = 's')
screen.onkey(fun = lewo, key = 'a')
screen.onkey(fun = prawo, key = 'd')
screen.onkey(fun = wyczysc, key = 'c')
screen.onkey(fun = pozycja_wyjsciowa, key = 'u')

screen.exitonclick()

