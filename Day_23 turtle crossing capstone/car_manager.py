from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
OUT_OF_SCREEN = -300


class CarManager(Turtle):
    # pass
    def __init__(self):
        # 汽車特性:矩形；自右向左移；多種顏色
        self.all_cars = []
        self.ran_num = 0
        self.level = 11

    def create_car(self):
        # 產生新的車輛
        self.ran_num = random.randint(1, self.level)
        if self.ran_num == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

            
    def move(self):
        # 從右往左移(x座標遞減)
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def move_increment(self):
        # 通關後提高移動速度
        self.level -= 1
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT)
            
    
    def remove(self):
        # 移除超過畫面的汽車
        for car in range(len(self.all_cars)-1, -1, -1):
            if self.all_cars[car].xcor() < OUT_OF_SCREEN:
                self.all_cars[car].hideturtle()
                del(self.all_cars[car])

    def show_up(self):
        # 出現在畫面中
        self.showturtle()
        self.move()
    
    def detect_collision(self, player):
        # 偵測與玩家碰撞
        for detect in range(len(self.all_cars) -1, -1, -1):
            if self.all_cars[detect].distance(player) < 30:
                return True
                
