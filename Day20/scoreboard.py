from turtle import Turtle
import os

class Scoreboard(Turtle):
    
    def __init__(self):
        with open("Day20/data.txt",mode="r") as file:
            self.high_score = int(file.read())
        self.counter = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.counter} High Score: {self.high_score}", 
                   align="center", font=("Arial", 24, "normal"))


    def increment(self):
        self.counter += 1
        self.update_scoreboard()

    def reset(self):
        if self.counter > self.high_score:
            self.high_score = self.counter
            with open("Day20/data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        
        self.counter = 0
        self.update_scoreboard()