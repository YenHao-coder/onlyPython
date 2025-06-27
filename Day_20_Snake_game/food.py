from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """定義食物類別與屬性"""
        super().__init__()
        self.shape("circle") #形狀
        self.penup() #無筆跡
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5) #大小
        self.color("orange") #顏色
        self.speed("fastest") #生成速度
        self.refresh() #重複生產
    
    def refresh(self):
        '''隨機位置可重複生產'''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y) #生成位置