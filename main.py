import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput(title="Guess the State",prompt="What is the another state's name?")
print(answer_state)



screen.exitonclick()