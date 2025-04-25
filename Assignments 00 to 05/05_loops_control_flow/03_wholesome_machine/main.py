def main():
    # Define the correct affirmation
    affirmation = "I am capable of doing anything I put my mind to."

    # Loop until the user types the affirmation correctly
    while True:
        user_input = input("Please type the following affirmation: " + affirmation + " ")

        if user_input == affirmation:
            print("That's right! :)")
            break  # Exit the loop when the correct affirmation is typed
        else:
            print("Hmmm That was not the affirmation.")

if __name__ == '__main__':
    main()
