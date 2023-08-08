from turtle import Turtle,Screen
screen= Screen()
class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.speed('fastest')
        self.x_positions = [-275,-230,-185,-140,-95,-50,-5,40,85,130,175,220,265]
        self.bricks = [[],[],[],[],[],[],[],[]]



    def yellow_bricks(self):
        for brick_index in range(0,13):
            brick = Bricks()
            brick.color('yellow')
            brick.goto(self.x_positions[brick_index],40)
            self.bricks[0].append(brick)

        for brick_index in range(0, 13):
            brick2 = Bricks()
            brick2.color('yellow')
            brick2.goto(self.x_positions[brick_index], 70)
            self.bricks[1].append(brick2)
    def green_bricks(self):
        for brick_index in range(0,13):
            brick = Bricks()
            brick.color('green')
            brick.goto(self.x_positions[brick_index],100)
            self.bricks[2].append(brick)


        for brick_index in range(0, 13):
            brick = Bricks()
            brick.color('green')
            brick.goto(self.x_positions[brick_index], 130)
            self.bricks[3].append(brick)


    def orange_bricks(self):
        for brick_index in range(0, 13):
            brick = Bricks()
            brick.color('orange')
            brick.goto(self.x_positions[brick_index], 160)
            self.bricks[4].append(brick)


        for brick_index in range(0, 13):
            brick = Bricks()
            brick.color('orange')
            brick.goto(self.x_positions[brick_index], 190)
            self.bricks[5].append(brick)



    def red_bricks(self):
        for brick_index in range(0, 13):
            brick = Bricks()
            brick.color('red')
            brick.goto(self.x_positions[brick_index], 220)
            self.bricks[6].append(brick)


        for brick_index in range(0, 13):
            brick = Bricks()
            brick.color('red')
            brick.goto(self.x_positions[brick_index], 250)
            self.bricks[7].append(brick)


    def clear_brick(self,ball):
        for brick in self.yellows[0]:
            if ball.distance(brick) < 30:
                self.yellows[0].remove(brick)
                brick.clear()
                ball.bounce_y()



