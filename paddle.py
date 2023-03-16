from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def move_up(self):
        yaxis = self.ycor()
        self.goto(self.xcor(), yaxis + 20)

    def move_down(self):
        yaxis = self.ycor()
        self.goto(self.xcor(), yaxis - 20)
