
import colorgram 
import turtle as t
import random
t.colormode(255) #顏色模式設置為 0 ~ 255

def color_extract():
    """提取圖片內色彩值, 依照RGB順序做成子集合, 再形成列表"""
    colors = colorgram.extract('painting.jpg', 35) # 從圖片提取顏色
    RGB=[] #顏色點列表

    for i in range(0, len(colors)): 
        part = () #空的RGB子集合
        number_of_color = colors[i].rgb #宣告圖片中rgb值
        part = (number_of_color.r, number_of_color.g, number_of_color.b) #將RGB值分別加入子集合
        RGB.append(part) #將子集合元素加入列表
    print(RGB) #印出圖片的RGB列表

color_list = [(239, 229, 213), (203, 161, 18), (217, 155, 70), (242, 230, 236), (49, 104, 158), (207, 151, 
182), (226, 207, 135), (187, 66, 39), (229, 234, 242), (162, 29, 36), (29, 28, 69), (232, 240, 234), (36, 
79, 40), (28, 67, 32), (143, 161, 183), (168, 43, 50), (76, 104, 77), (151, 30, 27), (150, 169, 152), 
(193, 93, 76), (219, 172, 193), (229, 174, 165), (181, 96, 102), (105, 125, 159), (51, 51, 88), (180, 189, 
210), (65, 34, 20), (113, 138, 114), (181, 199, 183), (67, 24, 39), (249, 195, 2), (75, 77, 20), (177, 
197, 203), (104, 136, 146), (35, 77, 87)]

def draw_hirst_painting():
    """畫出長與寬10*10, 大小20, 間距50的彩色點圖"""
    jimmy = t.Turtle()
    jimmy.speed("fastest") #最快移動
    jimmy.penup() #不描繪線條
    jimmy.hideturtle() #隱藏指標

    jimmy.setheading(225) 
    jimmy.forward(300) 
    jimmy.setheading(0) #以左下角為起點

    num_of_dots = 100 

    for dot_count in range(1,num_of_dots + 1):
        jimmy.dot(20, random.choice(color_list))
        jimmy.forward(50) #間隔50步畫1點, 隨機顏色與20大小

        if dot_count % 10 == 0: #是否畫完第一排
            jimmy.setheading(90)
            jimmy.forward(50)
            jimmy.setheading(180)
            jimmy.forward(500)
            jimmy.setheading(0) #往上走到第二排並且由左往右畫

    screen = t.Screen()
    screen.exitonclick() #點擊螢幕離開視窗
