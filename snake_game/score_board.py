from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"score: {self.score} ", False, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score} , False, align='center', font=('Arial', 24, 'normal')")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"score: {self.score} , high score is {self.high_score}, False,  align='center', font=('Arial', 24, 'normal')")

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", False, align='center', font=('Arial', 24, 'normal'))



