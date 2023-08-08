### creata canvas done
### create ball done
### create paddle done
### create blocks to be broken done

### create scoreboard done
### create lives done
### create board per round done

from turtle import Turtle, Screen
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from scoreboard import Scoreboard
import time

position = (0,-280)
ball_position = (0,-255)
paddle = Paddle(position)
bricks = Bricks()
ball = Ball(ball_position)
scoreboard = Scoreboard()

bricks.yellow_bricks()
bricks.green_bricks()
bricks.orange_bricks()
bricks.red_bricks()
# print(bricks.yellows)
screen = Screen()
screen.bgcolor('black')
screen.setup(width=650,height=700)
screen.title('Breakout')
screen.tracer(0)
screen.listen()
screen.onkeypress(fun=paddle.move_right,key='Right')
screen.onkeypress(fun=paddle.move_left,key='Left')
# screen.onkeypress(fun=ball.start_move, key='w')

# for _ in range(0,7)
lives = 3
game_is_on = True

while game_is_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    for brick_list in bricks.bricks:
        for brick in brick_list:
            if ball.distance(brick) < 30:
                ball.bounce_x()
                # ball.bounce_y()
                brick.hideturtle()
                x_axis_difference = ball.distance(brick)
                y_axis_difference = ball.distance(brick)
                if x_axis_difference > y_axis_difference:
                    # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                    ball.bounce_x()
                else:
                    # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                    ball.bounce_x()
                    ball.bounce_y()

                if brick.ycor() == 40 or brick.ycor() == 70:
                    scoreboard.increase_score(1)
                elif brick.ycor() == 100 or brick.ycor() == 130:
                    scoreboard.increase_score(3)
                elif brick.ycor() == 160 or brick.ycor() == 190:
                    scoreboard.increase_score(5)
                elif brick.ycor() == 220 or brick.ycor() == 250:
                    scoreboard.increase_score(7)


                ball.number_of_hits += 1
                brick_list.remove(brick)

        if len(brick_list) == 0 and scoreboard.score == 416:
            bricks.yellow_bricks()
            bricks.green_bricks()
            bricks.orange_bricks()
            bricks.red_bricks()
            ball.number_of_hits = 0


    if ball.number_of_hits == 4:
        ball.increase_speed()
    elif ball.number_of_hits == 12:
        ball.increase_speed()

    if ball.distance(paddle) <= 30 and ball.ycor() < 290:
        ball.bounce_y()

    if ball.ycor() > 290:
        ball.bounce_y()
    elif ball.ycor() < -330:
        ball.reset_position(ball_position)
        paddle.goto(position)
        scoreboard.decrease_lives()


    if ball.xcor() > 285 + 10 or ball.xcor() < -285 - 10:
        ball.bounce_x()

    if scoreboard.lives > 0:
        game_is_on = True
    else:
        game_is_on = False


    screen.update()

screen.exitonclick()