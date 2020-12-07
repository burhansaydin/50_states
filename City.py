from turtle import Turtle


class city(Turtle):

    def __init__(self, cities, x_cor, y_cor):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x_cor, y_cor)
        self.write(cities)
   # def score(self):

