import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

def capstone():
    # 執行遊戲
    jim = Player()
    car_manager = CarManager()
    score = Scoreboard()

    screen.listen()
    screen.onkey(jim.upwards, "Up")

    game_is_on = True
    
    while game_is_on:
        
        time.sleep(0.1)
        screen.update()
        
        car_manager.create_car()
        car_manager.move()
        car_manager.remove()

        # 判斷被撞
        if car_manager.detect_collision(jim):
            game_is_on = False
            score.game_over()
        
        # 判斷進下一關
        if jim.next_level():
            car_manager.move_increment()
            score.level_up()

    game_continue = input("Do you want to play again? press 'y' to restart the game, or press 'n' to exit the window on click: \n").lower()

    if game_continue == 'y':
        screen.clear()
        screen.tracer(0)
        capstone()
    else:
        screen.exitonclick()
    
    



capstone()
