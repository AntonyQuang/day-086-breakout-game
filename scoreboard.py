from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 340)
        self.write(self.score, align="center", font=("Courier", 60, "normal"))

    def point(self):
        self.score +=100
        self.update_scoreboard()

class ScoreboardBorder(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto((0, 320))
        self.setheading(0)
        self.shapesize(stretch_wid=0.8, stretch_len=50)
