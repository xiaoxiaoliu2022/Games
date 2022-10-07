from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

l_paddle = Paddle((-360, 0))
r_paddle = Paddle((360, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
while game_on:
    screen.update()
    # time.sleep(ball.move_speed)
    ball.move()
    if ball.xcor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_cneter()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_cneter()
        scoreboard.r_point()
#
# turtle = Turtle()
# turtle.hide()
# turtle.setheading(90)
# for i in range(40):
#     turtle.pendown()
#     turtle.forward(20)
#     turtle.penup()
#     turtle.forward(20




screen.exitonclick()