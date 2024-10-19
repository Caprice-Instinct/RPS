from functions import get_AI_guess

# Constants
# Options for the player
options = ["Rock", "Paper", "Scissors"]

# Initialising player and AI score
player_score = 0
AI_score = 0

# User prompt
prompt = "Rock, paper, scissors... "

# Modes that the game has
option_modes = ['Endless', 'Best to 3', 'Best series']

# Prompt user for the game mode
print("Which mode would you like to play: ")
for index, mode in enumerate(option_modes):
    print(f"{index + 1}. {mode}.")

user_mode = int(input())

# Choose game mode according to user choice
# Mode 1: Endless; to infinity or till user exits
if option_modes[user_mode-1] == option_modes[0]:
    while True:
        # Prompt player for an input
        player_input = input(prompt).title()

        # Get AI input
        a = get_AI_guess()
        print(f"AI chose {a}.")

        # Player choice vs AI choice
        if a == player_input:
            print("We are so similar! We tied")
        elif player_input == options[0]:
            if a == options[2]:
                player_score += 1
                print(f"{player_input} smashes {a}.")
            else:
                AI_score += 1
                print(f"{a} covers {player_input}.")

        elif player_input == options[1]:
            if a == options[0]:
                player_score += 1
                print(f"{player_input} covers {a}.")
            else:
                AI_score += 1
                print(f"{a} cuts {player_input}.")

        elif player_input == options[2]:
            if a == options[1]:
                player_score += 1
                print(f"{player_input} cuts {a}.")
            else:
                AI_score += 1
                print(f"{a} smashes {player_input}. ")
        else:
            break

# Mode 2: Best to 3; Game ends when either AI or player gets a score of 3
elif option_modes[user_mode-1] == option_modes[1]:
    # Condition to stop the game/program when either reach a score of 3
    while player_score < 3 and AI_score < 3:
        # Prompt player for input
        player_input = input(prompt).title()

        # Get AI input
        a = get_AI_guess()
        print(f"AI chose {a}.")

        # Player choice vs AI choice
        if a == player_input:
            print("We are so similar! We tied")
        elif player_input == options[0]:
            if a == options[2]:
                player_score += 1
                print(f"{player_input} smashes {a}.")
            else:
                AI_score += 1
                print(f"{a} covers {player_input}.")

        elif player_input == options[1]:
            if a == options[0]:
                player_score += 1
                print(f"{player_input} covers {a}.")
            else:
                AI_score += 1
                print(f"{a} cuts {player_input}.")

        elif player_input == options[2]:
            if a == options[1]:
                player_score += 1
                print(f"{player_input} cuts {a}.")
            else:
                AI_score += 1
                print(f"{a} smashes {player_input}. ")

# Mode 3: Best to n series; game/program runs till AI or player score reaches n
if option_modes[user_mode-1] == option_modes[2]:
    # Prompt player for n(the final score needed to win)
    best = int(input("To what score will we have a winner?"))

    # Condition to run the program/game as long as player or AI has score less than n
    while player_score < best and AI_score < best:
        # Prompts player for input
        player_input = input(prompt).title()

        # Get AI input
        a = get_AI_guess()
        print(f"AI chose {a}.")

        # AI choice vs Player choice
        if a == player_input:
            print("We are so similar! We tied")
        elif player_input == options[0]:
            if a == options[2]:
                player_score += 1
                print(f"{player_input} smashes {a}.")
            else:
                AI_score += 1
                print(f"{a} covers {player_input}.")

        elif player_input == options[1]:
            if a == options[0]:
                player_score += 1
                print(f"{player_input} covers {a}.")
            else:
                AI_score += 1
                print(f"{a} cuts {player_input}.")

        elif player_input == options[2]:
            if a == options[1]:
                player_score += 1
                print(f"{player_input} cuts {a}.")
            else:
                AI_score += 1
                print(f"{a} smashes {player_input}. ")

# Print the total score for player
print(f"Player got a score of {player_score}.")

# Print the total score for AI
print(f"AI got a score of {AI_score}.")

# Condition to check the winner
if player_score > AI_score:
    # Player wins
    print(f"Player won by {player_score - AI_score} points. Congratulations!")
elif AI_score > player_score:
    # AI wins
    print(f"AI won by {AI_score - player_score} points. Better luck next time!")
else:
    # Player and AI draw
    print("You tied with the AI!")