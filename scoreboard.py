from turtle import Turtle
from tkinter import messagebox
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        if messagebox.askyesno(title="Game Over", message="Do you want to play again?"):
            self.level = 1
            self.update_scoreboard()
            return True
        else:
            self.goto(0, 0)
            self.write(f"Game Over", align="center", font=FONT)
            return False



