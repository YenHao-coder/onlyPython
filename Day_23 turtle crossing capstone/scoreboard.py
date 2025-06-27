from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """ 記分板特性 """
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        """紀錄目前等級"""
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align = "center", font =FONT)
    
    def game_over(self):
        """ 顯示遊戲結束 """
        self.home()
        self.write("Game Over", align = "center", font =FONT)

    def level_up(self):
        """ 顯示目前關卡等級 """
        self.level += 1
        self.update_level()

    