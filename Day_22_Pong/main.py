from turtle import Screen
from paddle import Paddle
from ball import Ball
import time 
from scoreboard import Scoreboard
screen = Screen()

screen.title("Pong game")
screen.screensize(800, 600, "black")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()



screen.listen()
screen.onkey(r_paddle.move_upwards, "Up")
screen.onkey(r_paddle.move_downwards, "Down")
screen.onkey(l_paddle.move_upwards, "w")
screen.onkey(l_paddle.move_downwards, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.speed_up)
    screen.update()
    ball.move()

    # 偵測與牆壁碰撞
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #偵測與球板碰撞
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #偵測乒乓球出界並記錄對方得分
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
         
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
    
    #偵測分數並結束遊戲
    if score.l_score >= 21 or score.r_score >= 21:
        is_game_on = False
        




screen.exitonclick()
