from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.goto(0, 250)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} | {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, leftORright):
        if leftORright == 'left':
            self.l_score += 1
        elif leftORright == 'right':
            self.r_score += 1
        self.clear()
        self.update_scoreboard()