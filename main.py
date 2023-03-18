from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

time_speed = 0.1
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Classic Pong Game')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(time_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if time_speed == 0:
            pass
        else:
            time_speed -= 0.01
    
    #Detect if right paddle misses
    if ball.xcor() > 390:
        ball.ball_reset()
        scoreboard.increase_score('left')
        time_speed = 0.1

    #Detect if left paddle misses
    if ball.xcor() < -390:
        ball.ball_reset()
        scoreboard.increase_score('right')
        time_speed = 0.1

    #Detect winner
    if scoreboard.declare_winner():
        game_is_on = False

screen.exitonclick()