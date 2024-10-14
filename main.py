from random import *
from functions import get_AI_guess


options = ["Rock", "Paper", "Scissors"]


score = 0
AI_score = 0

prompt = "Rock, paper, scissors... "

while score < 2:
    player_input = input(prompt).title()
    a = get_AI_guess()
    print(f"AI chose {a}.")

    if a == player_input:
        print("We are so similar! We tied")
    elif player_input == options[0]:
        if a == options[2]:
            score += 1
            print(f"{player_input} smashes {a}.")
        else:
            print(f"{a} covers {player_input}.")

    elif player_input == options[1]:
        if a == options[0]:
            score += 1
            print(f"{player_input} covers {a}.")
        else:
            print(f"{a} cuts {player_input}.")

    elif player_input == options[2]:
        if a == options[1]:
            score += 1
            print(f"{player_input} cuts {a}.")
        else:
            print(f"{a} smashes {player_input}. ")
print(score)