from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Classic Pong Game')
screen.tracer(0)

right_paddle = Turtle()
right_paddle.penup()
right_paddle.color('white')
right_paddle.shape('square')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.goto(x=350, y=0)

def move_up():
    yaxis = right_paddle.ycor()
    right_paddle.goto(350, yaxis + 20)

def move_down():
    yaxis = right_paddle.ycor()
    right_paddle.goto(350, yaxis - 20)

screen.listen()
screen.onkey(move_up, 'Up')
screen.onkey(move_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()