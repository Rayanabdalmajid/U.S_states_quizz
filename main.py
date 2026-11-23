import turtle
import pandas

screen = turtle.Screen()
screen.setup(750,750)
screen.title("U.S. state game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()
states_x = pandas.Series(x_cor, index = states)
states_y = pandas.Series(y_cor, index = states)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                    prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(states_x[answer_state], states_y[answer_state])
        tim.write(answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

            if len(guessed_states) == 50:
                print("You won!")

states_to_learn = []
for item in states:
    if item not in guessed_states:
        states_to_learn.append(item)

df = pandas.DataFrame(states_to_learn, columns=["state"])
df.to_csv("states_to_learn.csv")