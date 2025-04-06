from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.write_score()
        

    def write_score(self):
        self.clear()
        self.goto(-235, 250)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "bold"))

    def increment_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 15, "bold"))
