from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_file()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def read_file(self):
        with open("data.txt") as data:
            self.high_score = int(data.read())

    def write_file(self):
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score}  High Score: {self.high_score}', align=ALIGMENT, font=FONT)

    def score_point(self):
        self.score += 1
        self.update_scoreboard()
