from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.r = 1
        self.update_s()

    def update_s(self):
        self.clear()
        self.write(f"LEVEL: {self.r}", align="left", font=FONT)

    def over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("family", 24, "bold"))
    def level_up(self):
        self.r += 1
        self.update_s()
