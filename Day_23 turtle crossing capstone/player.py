from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    #pass
    def __init__(self):
        """定義烏龜"""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def upwards(self):
        """往上走"""
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def next_level(self):
        """ 到達終點後 """
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
