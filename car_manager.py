from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.allcars = []
        self.speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        n = random.randint(1, 6)
        if n == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.allcars.append(car)

    def move_car(self):
        for car in self.allcars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
