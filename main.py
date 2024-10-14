from functions import get_AI_guess


options = ["Rock", "Paper", "Scissors"]
player_score = 0
AI_score = 0

prompt = "Rock, paper, scissors... "

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


print(f"Player got a score of {player_score}.")
print(f"AI got a score of {AI_score}.")

if player_score > AI_score:
    print(f"Player won by {player_score - AI_score} points. Congratulations!")

else:
    print(f"AI won by {AI_score - player_score} points. Better luck next time!")
