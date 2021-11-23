# usGame.py
#
# Python Bootcamp Day 25 - US States Game
# Usage:
#      In the input box, type the name of a states and hit ENTER.
#      If correct, that's state's name will be added to the map.
#      You win if you get all 50. If you can't think of all the states,
#      type exit and a CSV fill will be created and tell you the states you missed.
#
# Marceia Egler November 23, 2021

import turtle
import pandas as pd
from state_writer import State_writer
from score import Score

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = Score()
state_writer = State_writer()
guesses = []


df = pd.read_csv("50_states.csv")
states = df.state.to_list()


while score.score < 50:
    answer_state = screen.textinput(
        title=f"{score.score}/50 States Correct",
        prompt="What's another state name?",
    ).title()

    if answer_state in states:
        if answer_state in guesses:
            score.keep_score()
        else:
            guesses.append(answer_state)
            x = df.loc[df["state"] == answer_state, "x"].to_list()
            y = df.loc[df["state"] == answer_state, "y"].to_list()
            state_writer.draw(x[0], y[0], answer_state)
            score.raise_score()
    if answer_state == "Exit":
        missed = [state for state in states if state not in guesses]
        missed_df = pd.DataFrame(data=missed)
        missed_df.to_csv("missed_states.csv")
        break

turtle.mainloop()
