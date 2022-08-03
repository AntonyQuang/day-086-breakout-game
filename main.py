import time
from turtle import Screen
from paddle import Paddle
from blocks import Block
from ball import Ball

screen = Screen()
screen.setup(width=600, height=900)
screen.bgcolor("#30262E")
screen.title("Let's Play Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
# Setting up blocks
block_row_colors = ["#BF4B66",
                    "#C447A9",
                    "#5C47C4",
                    "#478EC4",
                    "#47C4A5",
                    "#47C44F",
                    "#BCC447",
                    "#C47B47",
                    "#C45E47"]
columns = 8
rows = len(block_row_colors)
for column in range(columns):
    x = -250 + 70*column
    for row in range(rows):
        y = 230 - 25*row
        Block((x, y), block_row_colors[row])

screen.listen()
screen.onkeypress(fun=paddle.go_left, key="Left")
screen.onkeypress(fun=paddle.go_right, key="Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.xcor() < -280 or ball.xcor() > 270:
        ball.wall_bounce()

    if ball.ycor() > 320:
        ball.ceiling_bounce()

    if ball.distance(paddle) < 30 and ball.ycor() > -440:
        ball.paddle_bounce()

    ball.move()

screen.exitonclick()

