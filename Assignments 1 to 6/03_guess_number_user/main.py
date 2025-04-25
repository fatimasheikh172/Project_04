import random

def user_guess(x):
    secret_number = random.randint(1, x)
    guess = 0
    tries = 0

    print(f"I'm thinking of a number between 1 and {x}. Can you guess it?")

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            tries += 1

            if guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"🎉 Congratulations! You guessed the number {secret_number} in {tries} tries!")

# Run the game
user_guess(100)
