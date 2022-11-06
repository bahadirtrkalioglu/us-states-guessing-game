import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_list = data["state"].to_list()
guessed_states = []


def state_check():
    for state in state_list:
        if answer_state == state:
            return True
    return False


FONT = ('Arial', 7, 'bold')

screen.tracer(0)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess The State {len(guessed_states)}/50",
                                    prompt="What's Another State's Name?").title()

    if answer_state == "Exit":
        break

    if state_check():
        row_data = data[data.state == answer_state]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x=int(row_data.x), y=int(row_data.y))
        new_turtle.write(arg=answer_state, font=FONT, align="center")
        guessed_states.append(answer_state)
        screen.update()

        state_list.remove(answer_state)

# States to learn...


unknown_state_dict = {
    "Unknown States": state_list
}
unknown_state_df = pandas.DataFrame(unknown_state_dict)

unknown_state_df.to_csv("unknown_states_file.csv")

print("Game is over! You can learn the cities that you don't know by opening unknown states file! ")
