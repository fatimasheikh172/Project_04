import random

# This sets how likely the done() function is to say "I'm done"
DONE_LIKELIHOOD = 0.2

# This function randomly decides whether to stop or not
def done():
    return random.random() < DONE_LIKELIHOOD

# This is the function you're supposed to complete
def chaotic_counting():
    # Start counting from 1 to 10
    for number in range(1, 11):
        # Before printing the number, check if we're done
        if done():
            # If done() says True, stop counting and exit the function
            return
        # If not done, print the number on the same line
        print(number, end=' ')

# Main function that runs first
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")


if __name__ == '__main__':
    main()
