from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(90)
        self.penup()
        self.go_to_starting_position()

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_to_starting_position(self):
        self.setpos(STARTING_POSITION)

    
