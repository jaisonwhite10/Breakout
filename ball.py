from turtle import Turtle, Screen
from paddle import Paddle

import time
screen = Screen()

class Ball(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.x_speed = -1
        self.moving_speed = 0.05
        self.number_of_hits = 0

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.speed('fastest')
        self.goto(new_x,new_y)

    # def move_left(self):
    #     new_x = self.xcor() - self.x_move
    #     new_y = self.ycor() + self.y_move
    #     self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= self.x_speed
        self.moving_speed *= 0.99

    def increase_speed(self):
        self.moving_speed *= 0.99

    def reset_position(self,position):
        self.goto(position)
        self.moving_speed = 0.1
        # self.bounce_x()



    def start_move(self):
        game_is_on = True
        return game_is_on

