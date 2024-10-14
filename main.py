from functions import get_AI_guess


options = ["Rock", "Paper", "Scissors"]
player_score = 0
AI_score = 0

prompt = "Rock, paper, scissors... "

option_modes = ['Endless', 'Best to 3', 'Best series']
print("Which mode would you like to play: ")
for index, mode in enumerate(option_modes):
    print(f"{index + 1}. {mode}.")

user_mode = int(input())

if option_modes[user_mode-1] == option_modes[1]:
    while player_score < 3 and AI_score < 3:
        player_input = input(prompt).title()
        a = get_AI_guess()
        print(f"AI chose {a}.")

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

elif option_modes[user_mode-1] == option_modes[0]:
    while True:
        player_input = input(prompt).title()
        a = get_AI_guess()
        print(f"AI chose {a}.")

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

if option_modes[user_mode-1] == option_modes[2]:
    best = int(input("To what score will we have a winner?"))
    while player_score < best and AI_score < best:
        player_input = input(prompt).title()
        a = get_AI_guess()
        print(f"AI chose {a}.")

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

print(f"Player got a score of {player_score}.")
print(f"AI got a score of {AI_score}.")

if player_score > AI_score:
    print(f"Player won by {player_score - AI_score} points. Congratulations!")

elif AI_score > player_score:
    print(f"AI won by {AI_score - player_score} points. Better luck next time!")
else:
    print("You tied with the AI!")