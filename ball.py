from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        

    def move(self):
        xaxis = self.xcor() + 10
        yaxis = self.ycor() + 10
        self.goto(xaxis, yaxis)