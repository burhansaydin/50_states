import turtle
import City
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
city = City
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
print(all_states)
guessed_states = []
score = 0
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",prompt="What is the another state's name?").title()

    screen.tracer(0)

    for each in all_states:
        if each == answer_state:
            score += 1
            guessed_states.append(each)
            info = data[data["state"] == each]
            x_cor = int(info["x"])
            y_cor = int(info["y"])
            city.city(each, x_cor, y_cor)
            screen.update()
            all_states.remove(answer_state)
    if answer_state == "Exit":
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv("missing_states_to_learn")

        break







screen.exitonclick()