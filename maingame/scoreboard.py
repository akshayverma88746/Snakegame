from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sc = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.sc}", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

    def inc_score(self):
        self.sc += 1
        self.clear()
        self.write(f"Score: {self.sc}", align="center", font=("Courier", 24, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 24, "normal"))
