from turtle import Screen
from paddle import Pad
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_pad = Pad((350,0))
l_pad = Pad((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down, "Down")
screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")




game_is_on = True
while game_is_on:
    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 320 and ball.distance(r_pad) < 40:
        ball.hit()
    elif ball.xcor() < -320 and ball.distance(l_pad) < 40:
        ball.hit()

    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.score_left()
    if ball.xcor() < -390:
        ball.reset_position() 
        scoreboard.score_right()

screen.exitonclick()