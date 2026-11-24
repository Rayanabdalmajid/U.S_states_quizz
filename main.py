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


guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                    prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        states_to_learn = [item for item in states if item not in guessed_states]
        df = pandas.DataFrame(states_to_learn, columns=["state"])
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(state_data.x.item(), state_data.y.item())
        tim.write(answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            if len(guessed_states) == 50:
                print("you win! You've guessed all 50 states!")




