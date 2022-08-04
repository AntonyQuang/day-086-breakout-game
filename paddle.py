from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("#8AD3EB")
        self.goto((0, -420))
        self.setheading(0)
        self.shapesize(stretch_wid=0.8, stretch_len=3)
        self.ondrag(self.follow_mouse)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def follow_mouse(self, x, y):
        self.ondrag(None)
        y = self.ycor()
        self.goto(x, y)
        self.ondrag(self.follow_mouse)
