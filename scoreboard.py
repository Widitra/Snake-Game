from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!!!", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
