from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        """記分板特性"""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updatescore()

    def updatescore(self):
        """更新雙方得分紀錄"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("arial", 80, "normal"))
    
    def l_point(self):
        """左方得分"""
        self.l_score += 1
        self.updatescore()
    
    def r_point(self):
        """右方得分"""
        self.r_score += 1
        self.updatescore()
