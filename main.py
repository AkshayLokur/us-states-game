import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the states in the U.S.A.")

image = "./blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
turtle.pu()


def print_state_name_on_map(state, x, y):
    t = turtle.Turtle()
    t.hideturtle()
    t.pu()
    t.goto(int(x), int(y))
    t.write(state)


# Read CSV
csv_dataframe = pandas.read_csv("50_states.csv")
states = csv_dataframe["state"].to_list()

guessed_states = []
while len(states) != len(guessed_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} states correct!",
                                    prompt="What's another state name?")

    if answer_state is None:
        print("Bye!")
        exit()
    else:
        answer_state = answer_state.title()
        if answer_state in states and answer_state not in guessed_states:
            print(f"Yay! You found {answer_state}!")
            guessed_states.append(answer_state)
            csv_row = csv_dataframe[csv_dataframe["state"] == answer_state]
            print_state_name_on_map(answer_state, csv_row["x"], csv_row["y"])
        else:
            print(f"Nope! '{answer_state}' is not a valid states in U.S.A. Try Again!")

screen.exitonclick()
