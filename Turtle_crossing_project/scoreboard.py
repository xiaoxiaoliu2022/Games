FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.goto(-280, 260)
        self.write(f"LEVEL: {self.level}", False, align='left', font=FONT)

    def level_increase(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL: {self.level}", False, align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", False, align='center', font=FONT)