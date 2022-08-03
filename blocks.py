from turtle import Turtle


class Block(Turtle):
    def __init__(self, POSITION, COLOR):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(POSITION)
        self.color(COLOR)
        self.shapesize(stretch_wid=0.8, stretch_len=3)