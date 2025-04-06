import turtle as t
from random import randrange, choice

t.colormode(255)

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.speed("fastest")

def random_color():
    return ((randrange(0,255), randrange(0,255), randrange(0,255)))

def draw_spirtogrpah(gap):
    for _ in range(360 // gap):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

draw_spirtogrpah(5)
















screen = t.Screen()
screen.exitonclick()