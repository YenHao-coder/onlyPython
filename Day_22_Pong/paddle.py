from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        """定義接球板特性"""
        super().__init__()
        self.shape("square") #生成長方形
        self.color("white")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position)

    def move_upwards(self):
        """往上移 20 px"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_downwards(self):
        """往下移 20px"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
