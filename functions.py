from random import randint


def get_AI_guess():
    """
    Randomizes AI input between the three options
    :return: randomized input(str)
    """
    options = ["Rock", "Paper", "Scissors"]

    comp_input = randint(0, 2)
    comp = options[comp_input]
    return comp