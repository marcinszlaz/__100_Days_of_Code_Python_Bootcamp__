from turtle import Turtle, Screen


FONT = ("Courier", 24, "normal")
res = Screen()
res.tracer(0)

class Scoreboard(Turtle):
    """wyniki i info o koncu gry"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.score = 0
        self.level(self.score)

    def level(self, score):
        self.goto(-250,250)
        self.score = score
        # res.update()
        self.write(f'Level: {self.score}',move = False, align = 'left', font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER Mr Turtle !', move = False, align = 'center',font = FONT)