from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def restart():
    tim.home()
    tim.clear()
def turn_left():
    tim.lt(90)
def turn_right():
    tim.rt(90)
def move_backwards():
    tim.bk(10)
def move_forwards():
    tim.fd(10)

screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = restart)

screen.listen()
screen.exitonclick()