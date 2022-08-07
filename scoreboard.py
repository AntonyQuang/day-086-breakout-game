from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 350)
        self.write(self.score, align="center", font=("Courier", 60, "normal"))

    def point(self):
        self.score +=100
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -200)
        self.write("GAME OVER", align="center", font=("Courier", 40, "normal"))
        self.goto(0, -230)
        self.write("Press Space to play again", align="center", font=("Courier", 20, "normal"))
        self.goto(0, -260)
        self.write("Click to exit", align="center", font=("Courier", 20, "normal"))

    def game_win(self):
        self.goto(0, -200)
        self.write("YOU WIN!", align="center", font=("Courier", 40, "normal"))
        self.goto(0, -230)
        self.write("Press Space to play again", align="center", font=("Courier", 20, "normal"))
        self.goto(0, -260)
        self.write("Click to exit", align="center", font=("Courier", 20, "normal"))

    def reset(self):
        self.clear()
        self.__init__()

    def welcome(self):
        self.goto(0, -150)
        self.write("Press Space to Play", align="center", font=("Courier", 20, "normal"))
        self.goto(0, -180)
        self.write("Drag the paddle with your mouse", align="center", font=("Courier", 20, "normal"))


class ScoreboardBorder(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto((0, 330))
        self.setheading(0)
        self.shapesize(stretch_wid=0.8, stretch_len=50)
