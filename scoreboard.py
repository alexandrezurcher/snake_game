from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.write(arg=f'Score: {self.score}',align="center", font=("Arial", 20, "normal"))


    def score_point(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}',align="center", font=("Arial", 20, "normal"))
