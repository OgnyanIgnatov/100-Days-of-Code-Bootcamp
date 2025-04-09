import turtle, pandas

STATES_COUNT = 50

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
score = 0
guessed_states = []

while score != STATES_COUNT:
    answer_state = screen.textinput(title=f"{score}/50", prompt="What's another state name?").title()

    if answer_state == "Exit":
        states_to_learn = [s for s in states if not s in guessed_states]

        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        
        break


    if answer_state in states:

        score += 1
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_x = data[data["state"] == answer_state].x
        state_y = data[data["state"] == answer_state].y
        t.goto(state_x.item(), state_y.item())
        t.write(answer_state, align="center", font=("Times New Roman", 6, "bold"))

