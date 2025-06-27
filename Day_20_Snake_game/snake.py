from turtle import Turtle
INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)] #設置方塊的位置
MOVING_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    """建立白色方塊並像蛇一樣堆成一列"""
    def __init__(self):
        '''定義物件與屬性'''
        self.segements = [] #為了使後面跟隨前面位置, 建立列表來控制
        self.create_snake() #此函數建立更多實例
        self.head = self.segements[0] #頭
    
    def create_snake(self):
        for position in INITIAL_POSITION:
            """建立白色方塊並堆疊成一列"""
            self.add_segement(position)
            
    
    def add_segement(self, position):
        new_segement = Turtle("square")
        new_segement.color("white")
        new_segement.penup()
        new_segement.goto(position)
        self.segements.append(new_segement)
    
    def extend(self):
        """吃到食物後增加身體長度"""
        self.add_segement(self.segements[-1].position())
        
    def move(self):
        '''移動蛇'''
        for seg_num in range(len(self.segements)-1, 0, -1):
            """後面的方塊往前面的方塊位置前進"""
            new_x = self.segements[seg_num - 1].xcor()
            new_y = self.segements[seg_num - 1].ycor()
            self.segements[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)
    
    def up(self):
        """往上走並且不允許調頭"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
