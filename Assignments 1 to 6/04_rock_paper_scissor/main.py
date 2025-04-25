import random

def play():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    user = input("Choose rock, paper or scissors: ").lower()

    if user not in choices:
        return "Invalid input. Choose rock, paper, or scissors."

    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Run the game
print(play())