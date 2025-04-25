import random

username = input("Enter the name: ")

print(f"\nHello {username}! Welcome to the Guessing Number Game🔢🤔\n")
print("____________________________")

# Generate a random number between 1 to 20
numbers = random.randint(1 , 20)

# use loop for playing in this game

# Start the game

while True:
    guess = int(input("Enter your guess number: "))

    if guess < numbers:
        print("Too Low! 😞 Please Try Again 🔄")
    
    elif guess > numbers:
        print("Too High! 😲 Please Try Again 🔄")

    else:
        print("\nCONGRATULATIONS! 🎉 You guessed the right number! 🥳\n")
        break

# Thank the player for playing
print("Thank you for playing this game! 😊\n")