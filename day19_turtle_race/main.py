from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "make a bet", prompt = "Which turtle will win the race?Enter the color: ")
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

position_y = -100
for turtle_index in range(len(color)):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    position_y += 30
    new_turtle.goto(x = -230, y = position_y)
    new_turtle.color(color[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor > 230:
            is_race_on = False
            winning color = turtle.pencolor()
            if winning color == user_bet:
                print(f"You 've won! The {winning color} turtle is the winner!")
            else:
                print(f"You 've lost! The {winning color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()