import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.turtle_move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.cars_move()
    for car in car_manager.cars:
        if car.distance(player) < 15:
            game_on = False
            scoreboard.game_over()

    if player.turtle_crossed():
        scoreboard.level_increase()
        player.go_to_start()
        car_manager.cars_speedup()







screen.exitonclick()