import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car = CarManager()
screen.listen()
screen.onkey(player.move, "w")
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_car()
    for cr in car.allcars:
        if cr.distance(player) < 20:
            game_is_on = False
            score.over()
    if player.ycor() > 290:
        player.win()
        score.level_up()
        car.speed_up()

screen.exitonclick()