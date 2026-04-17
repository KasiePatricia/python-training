import random

def get_choices():
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
      if computer == "scissors":
        print("Rock smashes scissors! You win!")
      else:
        print("Paper covers rock! You lose!")
    elif player == "paper":
      if computer == "rock":
        print("Paper covers rock! You win!")
      else:
        print("Scissors cut paper! You lose!")
    elif player == "scissors":
      if computer == "paper":
        print("Scissors cut paper! You win!")
      else:
        print("Rock smashes scissors! You lose!")
    elif player != "rock" and player != "paper" and player != "scissors":
        print("Invalid choice.")


# Main program
choices = get_choices()
check_win(choices["player"], choices["computer"])

