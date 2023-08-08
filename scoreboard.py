from turtle import Turtle

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(280,300)
        self.write(self.score,align='right',font=('Courier',20,'normal'))
        self.goto(200,300)
        self.write(f'lives: {self.lives}',align='right',font=('Courier',20,'normal'))

    def increase_score(self,score):
        self.score += int(score)
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()
