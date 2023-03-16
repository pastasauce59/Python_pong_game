from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        

    def move(self):
        xaxis = self.xcor() + self.x_move
        yaxis = self.ycor() + self.y_move
        self.goto(xaxis, yaxis)
    
    def bounce(self):
        self.y_move = -10