from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0) #關閉移動過程動畫後並手動調整畫面更新率

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    """完成移動後再刷新畫面產生流暢移動視覺效果"""
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    """偵測貪吃蛇與食物碰撞"""
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scoring()

    """偵測貪吃蛇與牆壁碰撞"""
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    """偵測貪吃蛇與尾巴碰撞"""
    for segment in snake.segements[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()







screen.exitonclick()
