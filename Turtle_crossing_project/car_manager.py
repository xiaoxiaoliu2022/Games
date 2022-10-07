COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_cars()
        self.cars_move()
        # self.cars_speedup()

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 2:

            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_x = 290
            new_y = random.randint(-240, 240)
            new_car.goto(new_x, new_y)
            self.cars.append(new_car)

    def cars_move(self):
        for car in self.cars:
            car.backward(self.speed)

    def cars_speedup(self):
        self.speed += MOVE_INCREMENT

