from random import randint


def get_AI_guess():
    options = ["Rock", "Paper", "Scissors"]

    comp_input = randint(0, 2)
    comp = options[comp_input]
    return comp