import random

def hangman():
    words = ['python', 'streamlit', 'developer', 'project', 'science']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    tries = 6
    guessed_letters = []

    print("Let's play Hangman!")

    while tries > 0 and '_' in guessed:
        print("\nWord:", ' '.join(guessed))
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct!")
        else:
            tries -= 1
            print("Wrong guess.")

    if '_' not in guessed:
        print(f"\n🎉 You won! The word was '{word}'.")
    else:
        print(f"\n😢 You lost! The word was '{word}'.")

# Run the game
hangman()