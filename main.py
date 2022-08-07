import time
from turtle import Screen
from paddle import Paddle
from blocks import Block
from ball import Ball
from scoreboard import Scoreboard, ScoreboardBorder

screen = Screen()
screen.setup(width=600, height=900)
screen.bgcolor("#30262E")
screen.title("Let's Play Breakout")
screen.tracer(0)

scoreboard = Scoreboard()
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
blocks = {}
for column in range(columns):
    x = -250 + 70*column
    for row in range(rows):
        y = 230 - 25*row
        blocks[Block((x, y), block_row_colors[row])] = (x, y)
ceiling = ScoreboardBorder()
screen.listen()
screen.update()
scoreboard.welcome()


def play_game():
    reset()
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        # Wall bounce
        if ball.xcor() < -280 or ball.xcor() > 270:
            ball.wall_bounce()

        if ball.ycor() > 320:
            ball.ceiling_bounce()

        if abs(ball.xcor() - paddle.xcor()) < 40 and abs(ball.ycor() - paddle.ycor()) < 12 and ball.ycor() > -440:
            ball.paddle_bounce()
        # Determines how the ball will bounce if it hits a block
        for block in blocks:
            if abs(ball.xcor() - block.xcor()) < 40 and abs(ball.ycor() - block.ycor()) < 12:
                # If the ball is moving to the right and hits the left side of the block, bounce horizontally
                if (ball.xcor()-block.xcor()) > 25 and ball.x_move < 0:
                    ball.wall_bounce()
                # If the ball is moving to the left and hits the right side of the block, bounce horizontally
                if (ball.xcor()-block.xcor()) < -25 and ball.x_move > 0:
                    ball.wall_bounce()
                # If the ball hits the bottom of the block, bounce vertically
                if ball.ycor() - block.ycor() < -4 and ball.y_move > 0:
                    ball.ceiling_bounce()
                # If the ball hits the top of the block, bounce vertically
                if ball.ycor() - block.ycor() > 4 and ball.y_move < 0:
                    ball.ceiling_bounce()
                block.goto(0, -500)
                scoreboard.point()


        ball.move()

        if ball.ycor() < -460:
            scoreboard.game_over()
            screen.onkey(play_game, "space")
            screen.exitonclick()
            game_is_on = False

        if scoreboard.score == len(blocks)*100:
            scoreboard.game_win()
            screen.onkey(play_game, "space")
            screen.exitonclick()
            game_is_on = False


def reset():
    screen.onclick(None)
    screen.onkey(None, "space")
    scoreboard.reset()
    # Put the blocks back to the starting positions
    for block in blocks:
        block.goto(blocks[block])
    ball.goto(0, -200)


game_is_on = True
screen.onkey(play_game, "space")

screen.mainloop()