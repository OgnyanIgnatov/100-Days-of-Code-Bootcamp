from turtle import Screen, Turtle
from player import Player
from car import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    if player.ycor() > 280:
        player.go_to_starting_position()
        car_manager.level_up()
        scoreboard.increment_score()
        

    for car in car_manager.all_cars:
        if player.distance(car) < 26:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
