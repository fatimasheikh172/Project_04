import random


def tell_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "What do you call cheese that isn't yours? Nacho cheese!"
    ]
    return random.choice(jokes)

print("Welcome to Joke Bot!")
input("Press Enter to hear a joke...")
print("\nHere's a joke for you:")
print(tell_joke())


if __name__ == "__main__":
    tell_joke()
