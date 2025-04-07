from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race?")
colors = ["red", "green", "blue", "purple", "orange", "yellow"]
turtles = []

i = 0
for color in colors:
    t = Turtle("turtle")
    t.penup()
    t.color(color)
    t.goto(x=-240, y=-100 + i)
    i += 30
    turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False

            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle won!")
            else:
                print(f"You have lost! The {winning_color} turtle won!")

        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)


screen.exitonclick()