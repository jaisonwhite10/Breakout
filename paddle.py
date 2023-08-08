from turtle import Turtle
# from ball import Ball

# ball = Ball()
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=0.75,stretch_len=2)
        self.penup()
        self.speed('fastest')
        self.goto(position)


    def move_right(self):
        # if self.heading() != 0:
        #     self.setheading(0)
        #     self.forward(20)
        new_x = self.xcor() + 20
        self.goto(new_x,self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x,self.ycor())